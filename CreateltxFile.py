#_*_ coding:utf-8 _*_ 
import os
import subprocess
directory_name = '.'


"""
注意两件事情:
1. 在 LaTeX 代码中不能有 % 号, 所有用于注释的百分号都失去了作用, 因为最后的代码将所有 LaTeX 代码变为
字符串, 如果存在百分号, 那么相当于将字符串后面的代码都注释了.
2. 最后好像中文会有问题, 有的中文能正常显示, 但是有的中文却不行. 因此, LaTeX 代码中最好只用英文.
"""
for dirname, subdirs, filenames in os.walk(directory_name):
    if filenames:
        for filename in filenames:
            if filename.endswith('.py') and filename != 'CreateltxFile.py':
                LaTeX_codes = r"""
                    \documentclass[a4paper, 10pt]{article}
                    \usepackage[UTF8]{ctex}
                    \usepackage[left=1.8cm, right=2.5cm, top=2cm, bottom=2cm]{geometry}
                    \usepackage{amsmath}
                    \usepackage{amssymb}
                    \usepackage{tikz}
                    \usetikzlibrary{fadings, positioning}
                    \definecolor{bg}{rgb}{0.95, 0.95, 0.95}
                    \usepackage{mdframed}
                    \usepackage[outputdir="""  \
                    + dirname.replace('\\', '/') \
                    + r"""]{minted}
                    \usepackage{tcolorbox}
                    \tcbuselibrary{documentation,minted}
                    \tcbset{listing engine=minted}
                    \usepackage{xspace}
                    \usepackage[font=small,skip=0pt]{caption}
                    \usepackage{fontspec}
                    \setmonofont{Source Code Pro}
                    \usepackage{parskip}
                    \usepackage{enumitem}
                    \setlist{
                        topsep=0.3em,
                        partopsep=0pt,
                        itemsep=0ex plus 0.1ex,
                        parsep=0pt,
                        leftmargin=1.5em,
                        rightmargin=0em,
                        labelsep=0.5em,
                        labelwidth=2em
                    }
                    \usepackage{hyperref}
                    \hypersetup{
                        colorlinks=true,
                        bookmarksnumbered=true,
                        filecolor=blue
                    }

                    \newenvironment{codeEntry}{\begin{list}{}{
                      \setlength{\leftmargin}{-3em}
                      \setlength{\itemindent}{0pt}
                      \setlength{\itemsep}{0pt}
                      \setlength{\parsep}{0pt}
                      \setlength{\rightmargin}{0pt}
                      }\item}{\end{list}}

                    \def\filename{"""  \
                    + os.path.join(dirname, filename).replace('\\', '/') \
                    + "}\n" \
                    r"""
                    \begin{document}
                    \hskip-3em{\Large\textbf{"""  \
                    + filename.replace('_', r'\_')  \
                    + "}}\n"  \
                    + r"""
                    \begin{codeEntry}
                    \inputminted{python}{\filename}
                    \end{codeEntry}
                    \end{document}
                    """
                # print LaTeX_codes
                # print LaTeX_codes.replace('\\n', '@@').replace('\n', '').replace('@@', '\\n').strip()
                with open('_Output.txt', 'w') as f:
                    si = subprocess.STARTUPINFO()
                    si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                    subprocess.call('xelatex -shell-escape -8bit -output-directory ' + dirname.replace('\\', '/') + ' -jobname ' + filename.strip('.py') + ' "' \
                                    + LaTeX_codes.replace('\\n', '@@').replace('\n', '').replace('@@', '\\n').strip() \
                                    + '"',
                                    # stdout = f, 
                                    # stderr = subprocess.STDOUT,
                                    # stdin = subprocess.PIPE,
                                    startupinfo = si)
    # break

