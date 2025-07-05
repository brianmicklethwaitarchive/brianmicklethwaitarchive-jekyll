{
  description = "Jekyll development environment for brianmicklethwaitarchive";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs = { self, nixpkgs }: let
    system = "x86_64-linux";
    pkgs = nixpkgs.legacyPackages.${system};
  in {
    devShells.${system}.default = pkgs.mkShell {
      name = "jekyll-dev";
      buildInputs = with pkgs; [
        ruby
        bundler
        libxml2 # For nokogiri
        libxslt # For nokogiri
        zlib    # For nokogiri
	uv  # for generating quotes
      ];
      shellHook = ''
        export GEM_HOME="$(pwd)/.gems"
        export PATH="$GEM_HOME/bin:$PATH"
        export BUNDLE_PATH="$GEM_HOME"
        export BUNDLE_BIN="$GEM_HOME/bin"

        # Check if gems are installed
        if ! bundle check > /dev/null; then
          echo "Gems not installed, running 'bundle install'..."
          bundle install
        else
          echo "Gems are already installed."
        fi

        echo "Jekyll development environment ready."
        echo "Run 'bundle exec jekyll serve' to start the server."
      '';
    };
  };
}
