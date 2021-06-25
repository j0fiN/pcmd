# Design and Inspiration
What inspired pcmd? What is its backbone? And how they helped to make the package better? 

## Backbone
### <a href="https://typer.tiangolo.com/" class="link" target="_blank">Typer</a>
Typer is a library for building CLI applications. It is based on Python 3.6+ type hints.  
Building CLIs has become 'Type few lines of code and run' using this library, and it has never been easier.
CLI built using **Typer** can also be easily scaled up in complexity.

!!! success "pcmd uses it for"
    For everything!   
    **pcmd** is completely developed using **Typer**.  
    
    It has also inspired in bringing more focus on type hinting.
    It is the perfect tool to build small and effective CLIs  
    (like **pcmd **)
    and it provides a comfortable pathway to scale it up into big CLIs without much headache.
      
    **Typer** also provides built-in command autocompletion to **pcmd**.

!!! Tip "Fun Fact!"
    The *complete documentation* and *the <a href="https://gitmoji.dev/" class="link" target="_blank">gitmoji</a> commits* of **pcmd** was also inspired by the 
    <a target="_blank" class="link" href="https://tiangolo.com/">author's</a> 
    great works in <a href="https://fastapi.tiangolo.com/" class="link" target="_blank">FastApi</a> 
    and <a href="https://typer.tiangolo.com/" class="link" target="_blank">Typer</a>

### <a href="https://pyyaml.org/wiki/PyYAMLDocumentation" class="link" target="_blank">PyYAML</a>
PyYAML is a YAML parser and emitter for Python.  
It is the most commonly used yaml parser in the language.

!!! success "pcmd uses it for"
    All the works related to `cmd.yaml`. The `inspect` command uses pyaml exceptions to handle syntax errors in `cmd.yaml`.

### <a href="https://pypi.org/project/Distance/" class="link" target="_blank">Distance</a>
Distance is a Utilities library for comparing sequences.

!!! success "pcmd uses it for"
    Finding the levenshtein distance to suggest custom commands when user inputs the wrong name
    (name that does not exist in cmd.yaml).


## Inspiration and Idea - From the author of pcmd.

"I needed a tool that could take away all my hassles in typing atrocious terminal commands to a 'write-once-run-anytime-with-just-a-few-words' system. I thought that this issue might not be only for me but for other developers too. I realized that if a tool could do that, it would increase our workflow to another extent."  
    
<p align="right">~ <a href="https://jofin-f-archbald.herokuapp.com/" class="link" target="_blank">Jofin F Archbald</a></p>