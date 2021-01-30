with import <nixpkgs> {};
let
  opencvGtk = opencv.override (old: { enableGtk2 = true; });
  pythonEnv = python3.withPackages (ps: [
    ps.numpy
    ps.opencv4
  ]);

in mkShell {
  buildInputs = [
    pythonEnv
    opencvGtk
    pkg-config
    gtk2
  ];
}
