Python code for creating a simple maze.

The program works by first creating an empty rectangle with both X and Y sizes being an odd integer of 7 or above.
Each even numbered point inside the rectangle is a potential starting point.
One of these starting points is chosen at random and checked to see if it hasn't already been used.
Then a direction is chosen at random and a new wall is created by moving in that direction until an existing wall is hit.
When no more starting points are available the maze is complete.

The maze can be printed to screen as text or saved as a JPEG. Please note the JPEG is the same size as the maze data array and is intended for use in 3D elevation maps.
