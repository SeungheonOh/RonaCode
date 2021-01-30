RonaCode
========

'RonaCode is Covid-inspired esoteric programming language. It is a stack-based, turing
complete language based on BrainF**k[1] with added functionalities and new keywords.

Motivation
==========

This project is NOT developed to arouse awareness of Covid-19 in the programming communities; it
is developed for the meme.

Interpreter Implementation
==========================

The 'RonaCode interpreter operates as an Just in time interpreter, NOT as simple trans-compiler. This means
it operates as it receives input, and the full code is not required on the initialization.
It utilizes multiple keyword stacks to keep track of nested loops(isolate-expose).

Keywords
========
=====(Stack Arithmetics)=====
  :Definition:
    co[ro]+na  -  adds to the stack, number of "ro" repeated determines the amount to add
    ma[as]*sk  -  removes from stack, number of "as" repeated determines the amount to subtract

  corororororona : adds 5 to the stack
  masask :         remove 2 from stack

  'RonaCode, unlike BF, allows Arithmetics to be single instructions for better readability.

=====(Pointer Movements)=====
  :Definition:
     more  -  move to the next pointer
     less  -  move to the previous pointer

  Precondition
  [0][0][0][0][0]  // memory blocks
      ^            // current pointer

  After Execution of "more"
  [0][0][0][0][0]  // memory blocks
         ^         // current pointer

  After Execution of "less"
  [0][0][0][0][0]  // memory blocks
   ^               // current pointer

=====(Loops)=====
  :Definition:
    isolate  -  Starts a loop
    expose   -  Ends a loop

  isolate mask expose // loop
  loops util the pointing value becomes 0

=====(IO)=====
  :Definition:
    achoo  -  prints the pointing value
    gasp   -  set current stack to given value

  [97][0][0][0][0]  // memory blocks
   ^                // current pointer

   achoo // prints "a"

Repository Structure
====================

examples    - 'RonaCode examples, read examples/README.txt for more information
bftorona.py - BF to 'RonaCode Trans-compiler
rona.py     - 'RonaCode interpreter, reads from file (REPL[2] planned)

How to Run
==========

On your command line:
python3 rona.py examples/fibo.rona

Credits
=======

https://en.wikipedia.org/wiki/Brainfuck - Basic BrainF**k structure definition
https://docs.python.org/3/              - Python3 Documentation(FileIO, Class Structure)

--------------------
1. https://en.wikipedia.org/wiki/Brainfuck
2. Read-Eval-Print-Loop, https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop
