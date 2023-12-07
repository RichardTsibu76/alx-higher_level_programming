#include "lists.h"

/**
 * print_python_list_info - This function prints info about list in python
 * @p: This clearly by definition a pointer to list
 * Return: This is a void keyword and does not return
 */
void print_python_list_info(PyObject *p)
{
	int integer_i;
	long int size = PyList_Size(p);
	PyListObject *list_obj = (PyListObject *)p;
	const char *Elm_type;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", list_obj->allocated);
	for (integer_i = 0; integer_i < size; integer_i++)
	{
		Elm_type = Py_TYPE(list_obj->ob_item[integer_i])->tp_name;
		printf("Element %d: %s\n", integer_i, Elm_type);
	}
}
