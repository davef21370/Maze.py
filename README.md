Python code for creating a simple maze.

The program works by first creating an empty rectangle with both X and Y sizes being an odd integer of 7 or above.
Each even numbered point inside the rectangle is a potential starting point.
One of these starting points is chosen at random and checked to see if it hasn't already been used.
Then a direction is chosen at random and a new wall is created by moving in that direction until an existing wall is hit.
When no more starting points are available the maze is complete.

The maze can be printed to screen as text or saved as a PNG. Please note the PNG is the same size as the maze data array and is intended for use in 3D elevation maps.

18.12.12
Bug fix to make maze print correctly on mazes with different X,Y dimensions.  Added variable for maximum wall size to stop overly long walls on larger mazes.  Sped up the main loop by a long way.  Image saves as PNG instead of JPEG to stop pixel loss.

Big thanks to -rst- and IanH for their feedback.
