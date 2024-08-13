#CHATGPT

import polib
import os

def compile_mo_files(po_file_path, mo_file_path):
    # Check if the .po file exists before attempting to compile
    if not os.path.exists(po_file_path):
        print(f"File {po_file_path} does not exist.")
        return

    # Create directories for the .mo file if they do not exist
    os.makedirs(os.path.dirname(mo_file_path), exist_ok=True)

    # Compile the .po file to .mo file
    po = polib.pofile(po_file_path)
    po.save_as_mofile(mo_file_path)
    print(f"Compiled {po_file_path} to {mo_file_path}")

# Paths to .po and .mo files
po_file_fr = 'langues/fr/LC_MESSAGES/messages.po'
mo_file_fr = 'langues/fr/LC_MESSAGES/messages.mo'
po_file_en = 'langues/en/LC_MESSAGES/messages.po'
mo_file_en = 'langues/en/LC_MESSAGES/messages.mo'

# Compile the .po files to .mo files
compile_mo_files(po_file_fr, mo_file_fr)
compile_mo_files(po_file_en, mo_file_en)