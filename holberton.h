#ifndef HOLBERTON_H
#define HOLBERTON_H

#include <stdarg.h>
#include <stdlib.h>
#include <unistd.h>
/**
 * struct format - print formats
 * @s: format char
 * @fptr: function to print
 */
typedef struct format
{
	char *s;
	void (*fptr)(va_list);
} fmt_t;

int _putchar(char c);
void print_char(va_list args);
#endif /* HOLBERTON_H */
