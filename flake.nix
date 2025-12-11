{
  description = "Stock Market Circulars Processing Pipeline Development Environment";

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
            # Core development tools
            curl
            git
            just
            
            # Python ecosystem
            python311
            uv  # Python dependency management
            
            # System libraries for Python packages
            gcc
            stdenv.cc.cc.lib  # libstdc++
            zlib
            
            # Go server
            go
            nodejs_20  # For Claude Code
            
            # Development utilities
            direnv
          ];

          shellHook = ''
            echo "🚀 Stock Market Circulars Processing Pipeline"
            echo "Python + uv + Claude + Go development environment"
            echo ""
            
            # Set up library paths for Python packages
            export LD_LIBRARY_PATH="${pkgs.stdenv.cc.cc.lib}/lib:${pkgs.zlib}/lib:$LD_LIBRARY_PATH"
            
            # Set up npm prefix for user-local installs
            export NPM_CONFIG_PREFIX="$HOME/.npm-global"
            export PATH="$NPM_CONFIG_PREFIX/bin:$PATH"
            
            # Create npm global directory if it doesn't exist
            mkdir -p "$NPM_CONFIG_PREFIX"
            
            # Install Claude Code if not available
            if ! command -v claude &> /dev/null; then
              echo "📦 Installing Claude Code..."
              npm install -g @anthropic-ai/claude-code
            else
              echo "✅ Claude Code available"
            fi
            
            echo ""
            echo "🔧 Available commands:"
            echo "  just pipeline    # Run RSS scraping & AI processing"
            echo "  just serve       # Start Go development server"
            echo "  just build       # Build Go server binary"
            echo "  just stats       # Show processing statistics"
            echo ""
            echo "📚 Documentation: README.md"
          '';
        };
      });
}