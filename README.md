




Bug: Django took base.html from allauth instead of the top base.html.
Fix: Remove blank space before file name.

Bug: Footer was overlapping content.
Fix: Removed Bootstrap class fixed-footer.

Bug: Site would not open.
Fix: Fixed typo in bag/urls.py from name=view to name=view_bag.

Bug: Module not found, could not open server.
Fix: Fixed typo in context.py to contexts.py.

Bug: Background in navbar would not cover the navbar when scrolling.
Fix: Added constant white background to navbar.