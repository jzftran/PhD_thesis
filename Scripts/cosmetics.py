#%%
import re, shutil, tempfile
import glob


def inplace_re(filename, pattern, replacement):

    with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp_file:
        with open(filename) as src_file:
            text = src_file.read()
            tmp_file.write(pattern.sub(replacement, text))


    # Overwrite the original file with the munged temporary file in a
    # manner preserving file attributes (e.g., permissions).
    shutil.copystat(filename, tmp_file.name)
    shutil.move(tmp_file.name, filename)





citation_pattern = re.compile(r' \n\\begin_inset CommandInset citation', flags=re.MULTILINE)
citation_replacement = r'\n\\begin_inset space ~\n\\end_inset\n\\begin_inset CommandInset citation'


single_letter_pattern = re.compile(r'(\s[a-zA-Z])\s')
single_letter_replacement = r'\1\n\\begin_inset space ~\n\\end_inset\n'


auto_reference_pattern = re.compile(r'( \n)+\\begin_inset Flex CT - auto cross-reference', flags=re.MULTILINE)
auto_reference_pattern_replacement = r'\n\\begin_inset space ~\n\\end_inset\n\\begin_inset Flex CT - auto cross-reference'

reference_pattern = re.compile(r' (\n\\begin_inset CommandInset ref)', flags=re.MULTILINE)
reference_pattern_replacement = r'\n\\begin_inset space ~\n\\end_inset\1'

reference_pattern_ERT = re.compile(r' (\n\\begin_inset ERT\nstatus open\n\n\\begin_layout Plain Layout\n\n\n\\backslash\nref)', flags=re.MULTILINE)
reference_pattern_replacement_ERT = r'\n\\begin_inset space ~\n\\end_inset\n\1'



inline_equation = re.compile(r' (\n\\begin_inset Formula)', flags=re.MULTILINE)
inline_replacement = r'\n\\begin_inset space ~\n\\end_inset\1'



for filepath in glob.iglob('../*.lyx'):
    print(filepath)
    inplace_re(filepath, citation_pattern, citation_replacement)
    inplace_re(filepath, single_letter_pattern, single_letter_replacement)
    inplace_re(filepath, auto_reference_pattern, auto_reference_pattern_replacement)
    inplace_re(filepath, reference_pattern_ERT, reference_pattern_replacement_ERT)
    inplace_re(filepath, reference_pattern, reference_pattern_replacement)
    inplace_re(filepath, inline_equation, inline_replacement)





# %%
