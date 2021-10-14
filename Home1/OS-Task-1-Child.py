# coding: utf-8

# In[1]:


import random
import os
import time
import sys


# In[2]:


args = sys.argv;
if (len(args) < 2):
    print("Incorrect argument's amount");
else:
    waiting_period = int(args[1]);
    print("Запущена программа Child в процессе с PID", os.getpid(),"с аргументом",waiting_period)
    time.sleep(waiting_period);
    exit_status = int(random.uniform(0, 2));
    print("Завершился процесс с PID",os.getpid());
    os._exit(exit_status);


# In[ ]:




