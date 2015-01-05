# encoding=utf-8
'''
同时讨论何时使用异常，何时用error code
'''



'''
10.14　Replace Error Code with Exception （以异常取代错误码）

某个函数返回一个特定的代码，用以表示某种错误情况。

改用异常。

    int withdraw(int amount) {
        if (amount > _balance)
            return -1;
        else {
            _balance -= amount;
            return 0;
        }
    }

    void withdraw(int amount) throws BalanceException {
        if (amount > _balance) throw new BalanceException();
        _balance -= amount;
    }

动机

和生活一样，计算机偶尔也会出错。一旦事情出错，你就需要有些对策。最简单的情况下，你可以停止程序运行，返回一个错误码。这就好像因为错过一班飞机而自杀一样（如果真那么做，哪怕我是只猫，我的九条命也早赔光了）。尽管我的油腔滑调企图带来一点幽默，但这种"软件自杀"选择的确是有好处的。如果程序崩溃代价很小，用户又足够宽容，那么就放心终止程序的运行好了。但如果你的程序比较重要，就需要以更认真的方式来处理。

问题在于：程序中发现错误的地方，并不一定知道如何处理错误。当一段子程序发现错误时，它需要让它的调用者知道这个错误，而调用者也可能将这个错误继续沿着调用链传递上去。许多程序都使用特殊输出来表示错误，Unix系统和C-based系统的传统方式就是以返回值表示子程序的成功或失败。

Java有一种更好的错误处理方式：异常。这种方式之所以更好，因为它清楚地将"普通程序"和"错误处理"分开了，这使得程序更容易理解--我希望你如今已经坚信：代码的可理解性应该是我们虔诚追求的目标。









I normally prefer exceptions because they have more contextual information and can convey (when properly used) the error to the programmer in a more clear fashion.

On the other hand error codes are more lightweight than exceptions but are harder to maintain and error checking can inadvertedly be omitted. They are harder to maintain because you have to keep a catalog with all error codes and then switch on the result to see what error was thrown. Error ranges can be of help here because if the only thing we are interested in is if we are in the presence of an error or not is simpler to check (with an HRESULT error code greater or equal to 0 is success and less than zero is failure). They can inadvertedly be ommitted because there is no programmatic forcing that the developer will check for error codes. On the other hand you cannot ignore exceptions.

To resume I prefer exceptions over error codes in almost all situations.

'''



'''
Returning error code needs the calling function to check for the return value. This adds another if condition to the calling code - which needs additional test case. Also the onus is on the calling code. if the calling code forgets to check for the value, then a error returned would be missed.

Exceptions don't need the immediate calling function to catch the exception. The catch could be anywhere up the call stack. If there is none, the system catches the exception and terminates the program. Error conditions don't get missed using exceptions.
'''