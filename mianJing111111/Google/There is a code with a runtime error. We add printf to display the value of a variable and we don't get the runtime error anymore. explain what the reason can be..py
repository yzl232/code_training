# encoding=utf-8
'''
There is a code with a runtime error. We add printf to display the value of a variable and we don't get the runtime error anymore. explain what the reason can be.
'''
# 功能：从buf所指内存区域的前count个字节查找字符ch。
'''
#include <cstdio>
#include <cstring>

int main() {
    const void* res = memchr("Syshsh Pavlik", 'p', 16);
    // printf("%p\n", res);  // uncomment this line and see what happens
    return !*(int*)res;
}
'''
# apple.
'''

Brilliant!

This doesn't require multithreading or lazy loading (plainly prints a variable). Althought the example is a bit contrived, it shows what may happen:

 the string you are passing to printf lands somewhere in the constant data section in the executable (like .rodata) and


 may influence the memory layout (for example, make the '\0' character nearer for a non-terminated string etc.).

 In this example, the 'p' found by memchr when the printf is uncommented is from "%p" passed to printf!



Such bugs also suffer from "works on my machine" reproduction hardness, because the strings in the read-only section may be reordered and realigned at the compiler's will (and they are most certainly not preserving the order they occur in the source file due to constant string duplicate elimination done by most compilers).

I wish I could +1 it, but some bug in careercup.com just redirects me to my Google account, and when I enter the password nothing happens.
'''