/*
Author: Josh Vocal
Description: Take a file as an arguement and count the total number of lines and words in the file
*/

#include <stdio.h>
#include <ctype.h>
#include <stdbool.h>

#define TRUE   1
#define FALSE  0 

int main()
{
  unsigned long wordcount = 0, linecount = 0, charcount = 0;
  int c, flag;

  flag = FALSE;
  linecount = wordcount = charcount = 0;
  while ((c = getchar()) != EOF)
  {
    ++charcount;
    if (c == '\n')
    {
      ++linecount;
    }
      
    if (c == ' ' || c == '\t' || c == '\n' || c == '\0' || (isalpha(c) == 0 && c != '\''))
    {
      flag = FALSE;
    }
    else if (flag == FALSE)
    {
      flag = TRUE;
      ++wordcount;
    }
  }
  printf( "%lu %lu %lu\n", charcount, wordcount, linecount );
  return 0;
}
