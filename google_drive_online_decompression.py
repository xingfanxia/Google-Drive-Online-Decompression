# -*- coding: utf-8 -*-
"""Google_Drive_Online_Decompression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16e0tv3LEkAFaYHmKH2H63Cg6rpCNWFky

# **第一步 绑定GoogleDrive**
"""

#@markdown  点击左侧按钮，授权绑定GoogleDrive
from google.colab import drive
drive.mount('/content/drive')

"""# **RAR**

# 查看单个RAR压缩文件的目录树
"""

#@markdown 点击左侧按钮，查看单个RAR压缩包里面的目录结构

#@markdown <font size="4" color=red><b>destination</b></font>  查看的RAR压缩包的路径（带.rar后缀）

destination =  "" #@param {type:"string"}
!unrar v "$destination"

"""# 查看目录下所有RAR压缩文件的目录树"""

#@markdown 点击左侧按钮，查看目录下所有RAR压缩包的目录结构

#@markdown <font size="4" color=red><b>destination</b></font>  要查看的目录的路径（不带.rar后缀）

destination =  "" #@param {type:"string"}
!unrar v "$destination/*.rar"

"""## 解压单个RAR压缩包 ****支持分压卷****"""

#@markdown 点击左侧按钮，解压单个RAR压缩包

#@markdown <font size="4" color=red><b>destination</b></font>  解压的文件的路径（带.rar后缀）

destination =  "" #@param {type:"string"}

#@markdown <font size="4" color=red><b>files</b></font>  解压文件的目的地(目录)

files = "" #@param {type:"string"}

#@markdown <font size="4" color=red><b>password</b></font>  解压密码（有就填写没有就不填）

password = "" #@param {type:"string"}

print("若没有设置密码则直接回车即可")

!unrar x -p"$password" -o+ "$destination" "$files"

"""## 批量解压RAR"""

#@markdown 点击左侧按钮，解压整个目录下多个RAR压缩包

#@markdown <font size="4" color=red><b>destination</b></font>  解压的文件的路径（不带.rar后缀）

destination =  ""  #@param {type:"string"}

#@markdown <font size="4" color=red><b>files</b></font>  解压文件的目的地(目录)

files = "" #@param {type:"string"}

#@markdown <font size="4" color=red><b>password</b></font>  解压密码（有就填写没有就不填，因为是批量！所以必须密码是统一的，否则必定报错！！！）

password = "" #@param {type:"string"}

print("若没有设置密码则直接回车即可")

!unrar x -p"$password" -o+ "$destination/*.rar" "$files"

"""# **ZIP**

# 查看单个ZIP压缩文件的目录树
"""

#@markdown 点击左侧按钮，查看单个ZIP压缩包的目录结构

#@markdown <font size="4" color=red><b>destination</b></font>  查看的文件的路径（带.zip后缀）

destination =  "" #@param {type:"string"}

!unzip -l "$destination"

"""# 查看多个ZIP压缩文件里面的目录树"""

#@markdown 点击左侧按钮，查看整个目录下ZIP压缩包的目录结构

#@markdown <font size="4" color=red><b>destination</b></font>  查看的文件夹的路径（不带.zip后缀）

destination =  "" #@param {type:"string"}

!unzip -l "$destination/*.zip"

"""### 解压单个ZIP压缩包 ****支持分压卷****"""

#@markdown 点击左侧按钮，解压单个ZIP压缩包

#@markdown <font size="4" color=red><b>destination</b></font>  解压的文件的路径（带.zip后缀）

destination =  "" #@param {type:"string"}

#@markdown <font size="4" color=red><b>files</b></font>  解压文件的目的地(目录)

files = "" #@param {type:"string"}

#@markdown <font size="4" color=red><b>password</b></font>  解压密码（有就填写没有就不填）

password = "" #@param {type:"string"}

print("若没有设置密码则直接回车即可")

!7z x -aoa "$destination" -P"$password" -o"$files"

"""## 批量解压ZIP"""

#@markdown 点击左侧按钮，解压整个目录下多个ZIP压缩包

#@markdown <font size="4" color=red><b>destination</b></font>  填入要解压的文件的路径（不带.zip后缀）

destination =  "" #@param {type:"string"}

#@markdown <font size="4" color=red><b>files</b></font>  解压文件的目的地(目录)

files = "" #@param {type:"string"}

#@markdown <font size="4" color=red><b>password</b></font>  解压密码（有就填写没有就不填，因为是批量！所以必须密码是统一的，否则必定报错！！！）

password = "" #@param {type:"string"}

print("若没有设置密码则直接回车即可")

!7z x -aoa "$destination/*.zip" -P"$password" -o"$files"

"""# **7Z**

# 查看单个7Z压缩文件的目录树
"""

#@markdown 点击左侧按钮，查看单个7Z压缩包的目录结构

#@markdown <font size="4" color=red><b>destination</b></font> 查看压缩包的路径（带.7z后缀）

destination =  "" #@param {type:"string"}

!7z l "$destination"

"""# 查看多个7Z压缩文件的目录树"""

#@markdown 点击左侧按钮，查看整个目录下7Z压缩包的目录结构

#@markdown <font size="4" color=red><b>destination</b></font>  查看目录的路径（不带.7z后缀）

destination =  "" #@param {type:"string"}

!7z l "$destination/*.7z.*"

"""## 解压单个7Z压缩包 ****支持分压卷****"""

#@markdown 点击左侧按钮，解压单个7Z压缩包

#@markdown <font size="4" color=red><b>destination</b></font>  解压的7Z压缩包的路径（带.7z后缀）

destination =  "" #@param {type:"string"}

#@markdown <font size="4" color=red><b>files</b></font>  解压压缩文件到文件夹目录(目的地)

files = "" #@param {type:"string"}

#@markdown <font size="4" color=red><b>password</b></font>  压缩密码（有就填写没有就不填）

password = "" #@param {type:"string"}

print("若没有设置密码则直接回车即可")

!7z x -aoa "$destination" -P"$password" -r -o"$files"

"""## 批量解压7z"""

#@markdown 点击左侧按钮，解压整个目录下多个7Z压缩包

#@markdown <font size="4" color=red><b>destination</b></font>  解压的文件目录的路径（不带.7z后缀）

destination =  "" #@param {type:"string"}

#@markdown <font size="4" color=red><b>files</b></font>  解压压缩文件到文件夹目录(目的地)

files = "" #@param {type:"string"}

#@markdown <font size="4" color=red><b>password</b></font>  压缩密码（有就填写没有就不填，因为是批量！所以必须密码是统一的，否则必定报错！！！）

password = "" #@param {type:"string"}

print("若没有设置密码则直接回车即可")

!7z x -aoa "$destination/*.7z" -P"$password" -o"$files"

"""#  <font color=red><b>**通用格式**</b></font>

# 查看单个压缩文件的目录树
"""

#@markdown 点击左侧按钮，查看单个压缩包的目录结构

#@markdown <font size="4" color=red><b>destination</b></font> 查看压缩包的路径（带.xxx后缀）

destination =  "" #@param {type:"string"}

!7z l "$destination"

"""# 查看多个压缩文件的目录树"""

#@markdown 点击左侧按钮，查看整个目录下压缩包的目录结构

#@markdown <font size="4" color=red><b>destination</b></font>  查看目录的路径（不带.xxx后缀）

destination =  "" #@param {type:"string"}

!7z l "$destination/*.*"

"""## 解压单个压缩包 ****支持分压卷****"""

#@markdown 点击左侧按钮，解压单个压缩包


#@markdown <font size="4" color=red><b>destination</b></font>  解压的7Z压缩包的路径（带.xxx后缀）

destination =  "" #@param {type:"string"}

#@markdown <font size="4" color=red><b>files</b></font>  解压压缩文件到文件夹目录(目的地)

files = "" #@param {type:"string"}

#@markdown <font size="4" color=red><b>password</b></font>  压缩密码（有就填写没有就不填）

password = "" #@param {type:"string"}

!7z x -aoa "$destination" -P"$password" -r -o"$files"

"""## 批量解压"""

#@markdown 点击左侧按钮，解压整个目录下多个压缩包

#@markdown <font size="4" color=red><b>destination</b></font>  解压的文件目录的路径（不带.xxx后缀）

destination =  "" #@param {type:"string"}

#@markdown <font size="4" color=red><b>files</b></font>  解压压缩文件到文件夹目录(目的地)

files = "" #@param {type:"string"}

#@markdown <font size="4" color=red><b>password</b></font>  压缩密码（有就填写没有就不填，因为是批量！所以必须密码是统一的，否则必定报错！！！）

password = "" #@param {type:"string"}

!7z x -aoa "$destination/*.*" -P"$password" -o"$files"