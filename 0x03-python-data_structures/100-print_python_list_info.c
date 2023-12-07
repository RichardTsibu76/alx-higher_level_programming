#include <stdio.h>
#include <Python.h>
/**
 * print_python_list_info - Prints information about python list in c lang.
 * @p: PyListObject
 */


void print_python_list_info(PyObject *p)
{
	long int integer_i = 0;
	PyListObject *my_list;

	my_list = (PyListObject *)p;
	printf("[*] Size of the Python List = %ld\n", my_list->ob_base.ob_size);
	printf("[*] Allocated = %ld\n", my_list->allocated);

	while (integer_i < my_list->ob_base.ob_size)
	{
		printf("Element %ld: %s\n", integer_i,
				my_list->ob_item[integer_i]->ob_type->tp_name);
		i++;
	}
}
