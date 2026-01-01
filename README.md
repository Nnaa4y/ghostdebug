# ghostdebug

Have you ever wanted to use Unity's Debug class in Python? Now it's possible
## INSTALLATION
```bash
pip install ghostdebug
```

## USAGE

First,import Types,Filteres and the main Debugger:

```python
from ghostdebug import Debug
from filter import Type,Filter
```

Then,create logs with different types:

```python
Debug.Log("Number = 7",Type.Info)
Debug.Log("Wrong input detected",Type.Warn)
Debug.Log("An error detected",Type.Error)
Debug.Log("Can't divide by zero",Type.Error_Info)
```
Note:
If you don't use this Types the program will print:
```console
TypeException : Type 'used_type' is not defined
```
display all logs in console:
```python
Debug.Show(Filter.All)
```
The output will:
```console
[INFO]:Number = 7
[WARN]:Wrong input detected 
[ERROR]:An error detected
[ERROR INFO]:Can't divide by zero
```
For save logs automatically named as log1.txt,log2.txt etc:
```python
Debug.Save_Log()
```
The file location will:

On windows:
```text
C:\\Users\\USER_NAME\\Debug Logs
```
On linux:
```text
/home/USER_NAME/Debug Logs
```
On MacOS:
```text
/Users/USER_NAME/Debug Logs
```



