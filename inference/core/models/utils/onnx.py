from typing import List, Tuple, Union, Dict
def has_trt(providers: List[Union[Tuple[str, Dict], str]]) -> bool:
    for p in providers:
        if isinstance(p, tuple):
            name = p[0]
        else:
            name = p
        if name == "TensorrtExecutionProvider":
            return True
    return False