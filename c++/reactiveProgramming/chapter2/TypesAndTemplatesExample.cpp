#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <typeinfo>

using namespace std;

template<typename T>
void EmitConsole(T value)
{
  cout << typeid(value).name() << ": " << value << endl;
}

template<typename T>
void EmitValues(T&& arg)
{
  EmitConsole(forward<T>(arg));
}

template<typename T1, typename... Tn>
void EmitValues(T1&& arg1, Tn&&... args)
{
  EmitConsole(forward<T1>(arg1));
  EmitValues(forward<Tn>(args)...);
}

int main()
{
  EmitValues(0, 2.5, "Hello World!", 4);
  return 0;
}
