# coding: utf-8

# In[7]:


import os
import random
import sys
import time


# In[8]:


args = sys.argv;
if (len(args) < 2):
    print("Количество аргументов некорректно");
else:
    n = int(args[1]);
    for i in range (0, n):
        pr = os.fork();
        if (pr > 0):
            if i==0:
                print("Запущена программа Parent с  PID",os.getpid());
        else:
            random_num = int(random.uniform(5, 11));
            os.execl("./OS-Task-1-Child.py", "OS-Task-1-Child.py", str(random_num));
            break;


# In[9]:


for i in range (0, n):
    callback = os.wait();
    print("Дочерний процесс с PID",callback[0],"завершился. Статус завершения",callback[0])


# In[ ]:




