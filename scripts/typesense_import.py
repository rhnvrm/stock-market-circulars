#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "requests",
# ]
# ///
"""
Typesense Import Script for Stock Market Circulars

This script imports Hugo-generated search data into Typesense for fast, 
typo-tolerant search functionality.

Usage:
    uv run --script scripts/typesense_import.py [--rebuild]
"""

import os
import sys
import json
import argparse
from pathlib import Path
from typing import List, Dict, Any

import requests

# Typesense configuration
TYPESENSE_CONFIG = {
    'host': os.getenv('TYPESENSE_HOST', 'localhost'),
    'port': int(os.getenv('TYPESENSE_PORT', '8108')),
    'protocol': os.getenv('TYPESENSE_PROTOCOL', 'http'),
    'api_key': os.getenv('TYPESENSE_API_KEY', 'xyz'),
    'collection_name': 'circulars'
}

class TypesenseImporter:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.base_url = f"{config['protocol']}://{config['host']}:{config['port']}"
        self.headers = {
            'X-TYPESENSE-API-KEY': config['api_key'],
            'Content-Type': 'application/json'
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)
    
    def check_health(self) -> bool:
        """Check if Typesense server is running and accessible"""
        try:
            response = self.session.get(f"{self.base_url}/health")
            return response.status_code == 200
        except requests.RequestException:
            return False
    
    def create_collection(self) -> bool:
        """Create the circulars collection schema"""
        schema = {
            'name': self.config['collection_name'],
            'fields': [
                {'name': 'circular_id', 'type': 'string', 'facet': False},
                {'name': 'title', 'type': 'string', 'facet': False},
                {'name': 'description', 'type': 'string', 'facet': False},
                {'name': 'content', 'type': 'string', 'facet': False},
                {'name': 'source', 'type': 'string', 'facet': True, 'index': True},
                {'name': 'category', 'type': 'string', 'facet': True, 'index': True},
                {'name': 'impact', 'type': 'string', 'facet': True, 'index': True},
                {'name': 'severity', 'type': 'string', 'facet': True, 'index': True},
                {'name': 'tags', 'type': 'string[]', 'facet': True, 'index': True},
                {'name': 'stocks', 'type': 'string[]', 'facet': True, 'index': True},
                {'name': 'date', 'type': 'string', 'facet': True},
                {'name': 'published_date', 'type': 'string', 'facet': False},
                {'name': 'url', 'type': 'string', 'facet': False},
                {'name': 'pdf_url', 'type': 'string', 'facet': False},
                {'name': 'rss_url', 'type': 'string', 'facet': False},
                {'name': 'timestamp', 'type': 'int64', 'facet': False}  # Add timestamp for sorting
            ],
            'default_sorting_field': 'timestamp'
        }
        
        try:
            response = self.session.post(f"{self.base_url}/collections", json=schema)
            if response.status_code == 201:
                print("✅ Collection created successfully")
                return True
            elif response.status_code == 409:
                print("ℹ️  Collection already exists")
                return True
            else:
                print(f"❌ Failed to create collection: {response.text}")
                return False
        except requests.RequestException as e:
            print(f"❌ Failed to create collection: {e}")
            return False
    
    def delete_collection(self) -> bool:
        """Delete the existing collection for rebuild"""
        try:
            response = self.session.delete(f"{self.base_url}/collections/{self.config['collection_name']}")
            if response.status_code == 200:
                print("✅ Collection deleted successfully")
                return True
            else:
                print(f"❌ Failed to delete collection: {response.text}")
                return False
        except requests.RequestException as e:
            print(f"❌ Failed to delete collection: {e}")
            return False
    
    def import_documents(self, documents: List[Dict[str, Any]]) -> bool:
        """Import documents into Typesense"""
        if not documents:
            print("⚠️  No documents to import")
            return False
        
        try:
            # Add timestamp field for sorting and map id to circular_id
            import datetime
            processed_documents = []
            for doc in documents:
                processed_doc = doc.copy()
                # Map id field to circular_id to avoid conflict with Typesense's internal id
                if 'id' in doc:
                    processed_doc['circular_id'] = doc['id']
                    del processed_doc['id']
                # Convert date string to timestamp
                try:
                    date_obj = datetime.datetime.strptime(doc.get('date', '2025-01-01'), '%Y-%m-%d')
                    processed_doc['timestamp'] = int(date_obj.timestamp())
                except (ValueError, TypeError):
                    processed_doc['timestamp'] = 1640995200  # Default to 2022-01-01
                processed_documents.append(processed_doc)
            
            # Import documents individually to avoid batching issues
            total_imported = 0
            
            for i, doc in enumerate(processed_documents):
                response = self.session.post(
                    f"{self.base_url}/collections/{self.config['collection_name']}/documents/import",
                    json=doc,
                    params={'action': 'upsert'}
                )
                
                if response.status_code == 200:
                    response_text = response.text.strip()
                    try:
                        result_json = json.loads(response_text)
                        if result_json.get('success', False):
                            total_imported += 1
                            if (i + 1) % 100 == 0:
                                print(f"✅ Imported {i + 1} documents...")
                        else:
                            print(f"❌ Import error for document {i + 1}: {result_json}")
                    except json.JSONDecodeError:
                        print(f"❌ Failed to parse import result for document {i + 1}: {response_text}")
                else:
                    print(f"❌ Failed to import document {i + 1}: {response.status_code} - {response.text}")
                    return False
            
            print(f"✅ Successfully imported {total_imported} documents")
            return True
            
        except requests.RequestException as e:
            print(f"❌ Failed to import documents: {e}")
            return False
    
    def load_search_data(self, data_path: Path) -> List[Dict[str, Any]]:
        """Load search data from Hugo-generated JSON file"""
        if not data_path.exists():
            print(f"❌ Search data file not found: {data_path}")
            return []
        
        try:
            with open(data_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                print(f"✅ Loaded {len(data)} documents from {data_path}")
                return data
        except json.JSONDecodeError as e:
            print(f"❌ Failed to parse JSON: {e}")
            return []
        except Exception as e:
            print(f"❌ Failed to load search data: {e}")
            return []
    
    def run(self, data_path: Path, rebuild: bool = False) -> bool:
        """Run the import process"""
        print(f"🔍 Typesense Importer")
        print(f"   Server: {self.base_url}")
        print(f"   Collection: {self.config['collection_name']}")
        print(f"   Data file: {data_path}")
        print()
        
        # Check server health
        if not self.check_health():
            print("❌ Typesense server not accessible")
            print("   Make sure Typesense is running: docker-compose up -d")
            return False
        
        # Load search data
        documents = self.load_search_data(data_path)
        if not documents:
            return False
        
        # Rebuild collection if requested
        if rebuild:
            print("🔄 Rebuilding collection...")
            if not self.delete_collection():
                return False
        
        # Create collection
        if not self.create_collection():
            return False
        
        # Import documents
        return self.import_documents(documents)

def main():
    parser = argparse.ArgumentParser(description='Import search data into Typesense')
    parser.add_argument(
        '--data-path', 
        type=Path, 
        default=Path('hugo-site/public/search.json'),
        help='Path to Hugo-generated search data file'
    )
    parser.add_argument(
        '--rebuild', 
        action='store_true',
        help='Delete and recreate the collection before importing'
    )
    parser.add_argument(
        '--host',
        help='Typesense server host (default: localhost)'
    )
    parser.add_argument(
        '--port',
        type=int,
        help='Typesense server port (default: 8108)'
    )
    parser.add_argument(
        '--api-key',
        help='Typesense API key'
    )
    
    args = parser.parse_args()
    
    # Update config with command line arguments
    config = TYPESENSE_CONFIG.copy()
    if args.host:
        config['host'] = args.host
    if args.port:
        config['port'] = args.port
    if args.api_key:
        config['api_key'] = args.api_key
    
    # Run importer
    importer = TypesenseImporter(config)
    success = importer.run(args.data_path, args.rebuild)
    
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()