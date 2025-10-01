
```
from typing import Final 
abc = "hihi"
abc = "hello"
print(abc)
```

- 변수를 변경할 수 있어서, 불안정함 

```
from typing import Final 
abc: Final[str] = "hihi"

print(abc)
```