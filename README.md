




Bug: Django took base.html from allauth instead of the top base.html.
Solve: Remove blank space before file name.

Bug: Footer was overlapping content.
Solve: Removed Bootstrap class fixed-footer.

Bug: Site would not open.
Solve: Fixed typo in bag/urls.py from name=view to name=view_bag.

Bug: Module not found, could not open server.
Solve: Fixed typo in context.py to contexts.py.