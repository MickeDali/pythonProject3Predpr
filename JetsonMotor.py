# to open/create a new html file in the write mode
f = open('templates/index.html', 'w')
# the html code which will go in the file GFG.html
html_template = """
<table width="400" border="1">
<tr>                
<td><p>Имя:</p><br /></td>
<td><p><input name="name" type="text" style="margin-top: 10px; margin-left: 10px; width:150px; height:50px;" /></p><br /></td>
</tr>

<tr>                   
<td><p>Фамилия:</p><br /></td>
<td><p><input surname="surname" type="text" style="margin-top: 10px; margin-left: 10px; width:150px; height:50px;" /></p><br /></td>
</tr>

<tr>                   
<td><p>Возраст:</p><br /></td>
<td><p><input age="age" type="text" style="margin-top: 10px; margin-left: 10px; width:150px; height:50px;" /></p><br /></td>
</tr>

<tr>                   
<td><br /></td>
<td>{{variable}}<p style="text-align: right;"><input type="submit" name="save" class="submit" value="     Сохранить     " /></p><br /></td>
</tr>

</table>
"""

# writing the code into the file
f.write(html_template)

# close the file
f.close()
