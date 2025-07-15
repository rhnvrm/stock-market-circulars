{
  description = "Stock Market Circulars Static Site Development Environment";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
      in
      {
        devShells.default = pkgs.mkShell {
          buildInputs = with pkgs; [
            # Core tools for RSS parsing and file processing
            curl
            wget
            xmlstarlet
            jq
            
            # Development utilities
            direnv
            git
            
            # Node.js for npm packages (Hugo will be installed via npm initially)
            nodejs_20
            
            # Shell scripting utilities
            bash
            coreutils
            findutils
            
            # PDF processing tools
            poppler_utils  # for pdftotext if needed
          ];

          shellHook = ''
            echo "🏗️  Stock Market Circulars Development Environment"
            echo "📦 Available tools:"
            echo "   - curl, wget: For downloading RSS feeds and files"
            echo "   - xmlstarlet: For RSS XML parsing"
            echo "   - jq: For JSON processing"
            echo "   - nodejs: For npm packages (Hugo installation)"
            echo ""
            echo "📁 Project structure will be:"
            echo "   ├── scripts/     # RSS scraper and processing scripts"
            echo "   ├── hugo-site/   # Hugo static site"
            echo "   ├── inbox/       # Downloaded circulars"
            echo "   └── state/       # Processing state files"
            echo ""
            echo "🚀 Run './scripts/fetch-circulars.sh' to start downloading circulars"
            echo "🔄 Run './scripts/process-all.sh' to process downloaded files"
          '';
        };
      });
}