#include <stdio.h>
 
void spiral_traverse( char* input_array, int rows, int columns ) {
  // Output Array Counters
  int i, j, k, r, c;  
  // Input Array Counter
  int l = 0;
 
  // Init Output Array
  char output_array[ rows ][ columns ];
  for( i = 0; i < rows; i++ ) {
    for( j = 0; j < columns; j++ ) {
      output_array[ i ][ j ] = 0;
    }
  }
 
  for( i = 0, c = columns - 1, r = rows - 1;  c >= 0 && r >= 0;  i++, c--, r-- ) {  
 
    // Traversing Forward
    for( k = i ; k <= c; k++ ) {
      if( l == rows * columns ) break;
      output_array[ i ][ k ] = input_array[ l++ ]; 
    }
 
    // Traversing Downward
    for( k = i + 1; k <= r; k++ ) { 
      if( l == rows * columns )	break;
      output_array[ k ][ c ] = input_array[ l++ ];
    }
 
    // Traversing Backward
    for( k = c - 1; k >= i; k-- ) { 
      if( l == rows * columns ) break;
      output_array[ r ][ k ] = input_array[ l++ ];
    }
 
    // Traversing Upward
    for( k = r - 1; k > i; k-- ) {
      if( l == rows * columns ) break;
      output_array[ k ][ i ] = input_array[ l++ ];
    }
 
  }
 
  // Traverse the Output Array Left-to-Right, Top-to-Bottom
  for( i = 0; i < rows; i++ ) {
    for( j = 0; j < columns; j++ ) {
      printf( "%d ", output_array[ i ][ j ] );
    }
    printf("\n");
  }
 
  printf( "\n" );
  return;
}
 
int main() {
 
  int i;
  int rows = 5;
  int columns = 6;
  char input_array[ rows * columns ];
 
  for( i = 0; i < rows * columns; i++ ) {
    input_array[ i ] = i;
  }
 
  spiral_traverse( input_array, rows, columns );
 
  return 0;
}
