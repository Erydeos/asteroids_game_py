{ pkgs ? import <nixpkgs> {} }:
pkgs.mkShell {
  packages = [ pkgs.python313 pkgs.uv ];

  LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [
    pkgs.stdenv.cc.cc.lib
    pkgs.zlib
    pkgs.libGL
    pkgs.wayland
    pkgs.libxkbcommon
    pkgs.libdecor
    pkgs.libX11
    pkgs.libXext
    pkgs.libXcursor
    pkgs.libXi
    pkgs.libXrandr
    pkgs.libXfixes
    pkgs.libXScrnSaver
    pkgs.libXxf86vm
  ];

  UV_PYTHON_DOWNLOADS = "never";
}
