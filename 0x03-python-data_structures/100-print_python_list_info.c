#include <stdio.h>
#include <Python.h>
/**
 * print_python_list_info - A C function that prints some
 *                         basic info about Python lists
 * @p: A PyObject to be type-cast to PyListObject
 */


void print_python_list_info(PyObject *p)
{
	long int i = 0;
	PyListObject *my_list;

	my_list = (PyListObject *)p;
	printf("[*] Size of the Python List = %ld\n", my_list->ob_base.ob_size);
	printf("[*] Allocated = %ld\n", my_list->allocated);

	while (i < my_list->ob_base.ob_size)
	{
		printf("Element %ld: %s\n", i,
				my_list->ob_item[i]->ob_type->tp_name);
		i++;
	}
}
