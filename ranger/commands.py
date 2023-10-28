from __future__ import absolute_import, division, print_function

import os

from ranger.api.commands import Command


class Env(Command):
    name = "env"

    def execute(self):
        env = self.rest(1)
        if env in os.environ:
            self.fm.notify(f"{env}: {os.environ[env]}")
        else:
            self.fm.notify("Not found", bad=True)
        return

    def tab(self, tabnum):
        envs = (e for e in os.environ if e.startswith(self.rest(1)))
        return (self.start(1) + e for e in envs)


class Ntfy(Command):
    name = "ntfy"

    def execute(self):
        import requests
        from dotenv import load_dotenv

        load_dotenv()
        token = os.getenv("NTFY_TOKEN")

        url = "https://ntfy.rodrigokimura.com/test"
        data = self.rest(1).strip()
        if not data:
            self.fm.notify("No message", bad=True)
        headers = {
            "Authorization": f"Bearer {token}",
            "Title": "From ranger",
            "Priority": "high",
        }
        response = requests.post(url, data, headers=headers)
        if response.ok:
            self.fm.notify("Sent!")
        else:
            self.fm.notify(f"Error: {response.content.decode()}")


class my_edit(Command):
    # The so-called doc-string of the class will be visible in the built-in
    # help that is accessible by typing "?c" inside ranger.
    """:my_edit <filename>

    A sample command for demonstration purposes that opens a file in an editor.
    """

    # The execute method is called when you run this command in ranger.
    def execute(self):
        # self.arg(1) is the first (space-separated) argument to the function.
        # This way you can write ":my_edit somefilename<ENTER>".
        if self.arg(1):
            # self.rest(1) contains self.arg(1) and everything that follows
            target_filename = self.rest(1)
        else:
            # self.fm is a ranger.core.filemanager.FileManager object and gives
            # you access to internals of ranger.
            # self.fm.thisfile is a ranger.container.file.File object and is a
            # reference to the currently selected file.
            target_filename = self.fm.thisfile.path

        # This is a generic function to print text in ranger.
        self.fm.notify("Let's edit the file " + target_filename + "!")

        # Using bad=True in fm.notify allows you to print error messages:
        if not os.path.exists(target_filename):
            self.fm.notify("The given file does not exist!", bad=True)
            return

        # This executes a function from ranger.core.acitons, a module with a
        # variety of subroutines that can help you construct commands.
        # Check out the source, or run "pydoc ranger.core.actions" for a list.
        self.fm.edit_file(target_filename)

    # The tab method is called when you press tab, and should return a list of
    # suggestions that the user will tab through.
    # tabnum is 1 for <TAB> and -1 for <S-TAB> by default
    def tab(self, tabnum):
        # This is a generic tab-completion function that iterates through the
        # content of the current directory.
        return self._tab_directory_content()
