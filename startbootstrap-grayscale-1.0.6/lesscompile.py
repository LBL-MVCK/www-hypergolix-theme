import lesscpy

# with open('less/grayscale.less', 'r') as f:
#     precompile = f.read()
    
# with open('less/prepend.css', 'r') as f:
#     prepend = f.read()
    
# compiled = prepend + lesscpy.compile('less/grayscale.less')
compiled = lesscpy.compile('less/grayscale.less')

with open('standardize.css', 'w') as f:
    f.write(compiled)