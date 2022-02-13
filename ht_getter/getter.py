'''
Copyright 2022 Rairye

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''

valid_hash_tag_char_classes = set(["ALPHA", "DIGIT", "UNDERSCORE"])
alpha_numeric_char_classes = set(["ALPHA", "DIGIT"])


invalid_numbers = set(['⓪', '①', '②', '③', '④', '⑤', '⑥', '⑦', '⑧', '⑨',  '🄋', '➀', '➁', '➂', '➃', '➄', '➅', '➆', '➇', '➈',
                       '⓿', '❶', '❷', '❸', '❹', '❺', '❻', '❼', '❽', '❾', '🄌', '➊', '➋', '➌', '➍', '➎', '➏', '➐', '➑', '➒',
                       '⓵', '⓶', '⓷', '⓸', '⓹', '⓺', '⓻', '⓼', '⓽', '🄀', '⒈', '⒉', '⒊', '⒋', '⒌', '⒍', '⒎', '⒏', '⒐', '⑴', '⑵', '⑶', '⑷', '⑸', '⑹', '⑺', '⑻', '⑼', '🄀', '🄁', '🄂', '🄃', '🄄', '🄅', '🄆', '🄇', '🄈', '🄉', '🄊',
                       '①', '②', '③', '④', '⑤', '⑥', '⑦', '⑧', '⑨', '⑴', '⑵', '⑶', '⑷', '⑸', '⑹', '⑺', '⑻', '⑼', 
                       '⓪', '⓵', '⓶', '⓷', '⓸', '⓹', '⓺', '⓻', '⓼', '⓽', '⓿', '⁰', '₀', '⓪', '①', '②', '③', '④', '⑤', '⑥', '⑦', '⑧', '⑨', '⓵', '⓶', '⓷', '⓸', '⓹', '⓺', '⓻', '⓼', '⓽',
                       '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹', '₁', '₂', '₃', '₄', '₅', '₆', '₇', '₈', '₉', '⑩', '⑪', '⑫', '⑬', '⑭', '⑮', '⑯', '⑰', '⑱', '⑲', '⑳', '➉', '➓', '⓾', '⒑', '⒒', '⒓',
                       '⒔', '⒕', '⒖', '⒗', '⒘', '⒙', '⒚', '⒛', '⑩', '⑪', '⑫', '⑬', '⑭', '⑮', '⑯', '⑰', '⑱', '⑲', '⑳', '⑽', '⑾', '⑿', '⒀', '⒁', '⒂', '⒃', '⒄', '⒅', '⒆', '⒇',
                       '⒑', '⒒', '⒓', '⒔', '⒕', '⒖', '⒗', '⒘', '⒙', '⒚', '⒛'
                       
    ])

def get_char_class(char):
    if char.isalpha():
        return "ALPHA"

    elif char.isspace():
        return "WHITESPACE"

    elif char.isdigit():
        if char in invalid_numbers:
            return "OTHER"
        else:
            return "DIGIT"

    elif char == "#":
        return "POUND"

    elif char == "_":
        return "UNDERSCORE"

    else:
        return "OTHER"
        
def get_hash_tags(source, mode = "strings"):        
    results = []

    if type(source) != str:
        return results

    mode = "strings" if type(mode) != str or mode != "indices" else "indices"

    last_valid_pound_sign = None
    possible_hash_tag = False
    last_char_class = None
    alphanumeric_count = 0
    source_len = len(source)
    
    for i in range(source_len):
        current_char_class = get_char_class(source[i])
        
        if current_char_class  == "POUND":
                if alphanumeric_count > 0 and last_valid_pound_sign != None:
                        results.append(source[last_valid_pound_sign: i] if mode == "strings" else [last_valid_pound_sign, i])

                last_valid_pound_sign = i
                possible_hash_tag = True   
                alphanumeric_count = 0
                
        else:
            if possible_hash_tag == True:
                if current_char_class in valid_hash_tag_char_classes:
                    if current_char_class in alpha_numeric_char_classes:
                        alphanumeric_count+=1
                else:
                    if alphanumeric_count > 0 and last_valid_pound_sign != None:
                        results.append(source[last_valid_pound_sign: i] if mode == "strings" else [last_valid_pound_sign, i])
                        
                    possible_hash_tag = False
                    alphanumeric_count = 0
                    last_valid_pound_sign = None
                    
        last_char_class = current_char_class

    if possible_hash_tag == True:
        if alphanumeric_count > 0:
            results.append(source[last_valid_pound_sign:] if mode == "strings" else [last_valid_pound_sign, source_len])


    return results
