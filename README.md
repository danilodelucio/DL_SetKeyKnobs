# DL_SetKeyKnobs
 Store different knob values and set all their keyframes at the same time.
 --------------------------------------------------------------------------------------------------------
 
 <p><em>- Storing the Knobs;</em></p>

![03](https://user-images.githubusercontent.com/47226196/158734232-81be930c-d2a5-461e-82fa-94ae9dc881af.png)

<p><em>- Showing registered Knobs on Script Editor;</em></p>

![04](https://user-images.githubusercontent.com/47226196/158734670-8b02aa11-d0de-4e35-abb0-a58b85fc1df7.png)

<p><em>- Setting the keyframes for all registered Knobs using the options menu or shortcut (you can change the shortcut for whatever you want);</em></p>

![02](https://user-images.githubusercontent.com/47226196/158734216-a222be90-b997-4a1f-b245-180fe2a00d78.png)

![05](https://user-images.githubusercontent.com/47226196/158736515-ef9e249e-98af-4d9a-8ef7-09dcc64460b6.png)

--------------------------------------------------------------------------------------------------------
# HOW TO INSTALL
 To download from Github, click on the green button (called <strong>Code</strong>), then click on "Download ZIP".
Probably the folder should be named as <strong>"DL_SetKeyKnobs-main"</strong>, so rename it as <strong>"DL_SetKeyKnobs"</strong> (if necessary), 
then move it to your <strong>".nuke"</strong> directory.

 In your <strong>".nuke"</strong> folder, open the files <strong>"init.py"</strong> and <strong>"menu.py"</strong>. If it doesn't exist, just simply create a new
<strong>"txt"</strong> file, give their respective names, and put <strong>".py"</strong> as an extension (for both files).

![01](https://user-images.githubusercontent.com/47226196/158733248-4f46da14-88a1-4875-8aaa-03eb5d8e2ca7.png)

 In your <strong>"init.py"</strong>:
<p><code>nuke.pluginAddPath('./DL_SetKeyKnobs')</code>

 In your </strong>"menu.py"</strong>:
<p><code>from DL_SetKeyKnobs import *</code>
<blockquote>
 You just to need to make sure that your folder (<strong>"DL_SetKeyKnobs"</strong>), has the same name and the same 
directory when you are setting in your <strong>"init.py"</strong>.
</blockquote>

--------------------------------------------------------------------------------------------------------
# IF YOU DON'T WANT TO INSTALL
 Just click on <strong>"DL_SetKeyKnobs.py"</strong> file (here on Github), then copy all the content, paste on <strong>Script Editor</strong> in Nuke, and execute it.
 
 The Tool will be generated on your Toolbar, and you can use it temporarily while your Nuke is open.
 
 --------------------------------------------------------------------------------------------------------
<strong>
Author: Danilo de Lucio
<p>Website: www.danilodelucio.com
<p>March/2022
</strong>
