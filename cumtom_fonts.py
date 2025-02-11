from art import *
from tqdm import tqdm
import random

LOREM = "Onceuponatimetherewasadearlittlegirlwhowaslovedbyeveryonewholookedather,butmostofallbyhergrandmother,andtherewasnothingthatshewouldnothavegiventothechild.Onceshegaveheralittlecapofredvelvet,whichsuitedhersowellthatshewouldneverwearnanythingelse;soshewasalwayscalledLittleRed-Cap.Onedayhermothersaidtoher,Come,LittleRed-Cap,hereisapieceofcakeandabottleofwine;takethemtoyourgrandmother,sheisillandweak,andtheywilldohergood.Setoutbeforeitgetshot,andwhenyouaregoing,walknicelyandquietlyanddonotrunoffthepath,oryoumayfallandbreakthebottle,andthenyourgrandmotherwillgetnothing;andwhenyougointoherroom,don'tforgettosay,Good-morning,anddon'tpeepintoeverycornerbeforeyoudoit.Iwilltakegreatcare,saidLittleRed-Captohermother,andgaveherhandonit.Thegrandmotherlivedoutinthewood,halfaleaguefromthevillage,andjustasLittleRed-Capenteredthewood,awolfmether.Red-Capdidnotknowwhatawickedcreaturehewas,andwasnotatafraidofhim.Good-day"

def text_filled_font(input, text=LOREM):
    def fill_word_with_text(text, ascii_art):
        # Split the ascii_art into lines without stripping leading spaces (which are important for alignment)
        word_shape = [line.rstrip('\n') for line in ascii_art.splitlines() if line]

        text_len = len(text)
        idx = 0
        height = len(word_shape)
        width = max(len(row) for row in word_shape)

        # Create an empty canvas: one character per cell.
        canvas = [[' ' for _ in range(width)] for _ in range(height)]

        # Fill the canvas using the shape: each non-space cell gets the next text character.
        for y in range(height):
            row = word_shape[y].ljust(width)  # pad the row to ensure it is as wide as the maximum row
            for x, ch in enumerate(row):
                if ch != ' ':
                    canvas[y][x] = text[idx % text_len]
                    idx += 1

        # Join the canvas rows into strings and then into one output string.
        filled_word_shape = [''.join(row) for row in canvas]
        return '\n'.join(filled_word_shape)
    # Using text2art to generate the ASCII art
    ascii_art = text2art(input, font="doh")

    # Call the function to get the filled word shape as a single string
    filled_ascii_art = fill_word_with_text(text, ascii_art)

    # Output the filled ASCII art
    return filled_ascii_art


def spectial_tokens_font_model(text, Model="GPT4o"):
      token = None
      tokens_dict = {
        "GPT4o": "<|EOS|>",
        "o1": "<|EOS|>",
        "o3": "<|EOS|>",
        "Llama32": "<|eot_id|>",
        "Llama31": "<|eot_id|>",
        "Phi3": "<|end|>",
        "Gemma2": "<code>",
        "Mistral": "[INST]", 
        }
      token = tokens_dict[Model]
# Define the <|EOS|> patterns for each character with a 10x10 grid
      my_patterns = {
      'A': ["          <|EOS|>          ", 
            "      <|EOS|><|EOS|>       ", 
            "     <|EOS|>   <|EOS|>     ", 
            "    <|EOS|>     <|EOS|>    ", 
            "   <|EOS|>       <|EOS|>   ", 
            "  <|EOS|><|EOS|><|EOS|>    ", 
            " <|EOS|>           <|EOS|> ", 
            "<|EOS|>             <|EOS|>", 
            "<|EOS|>             <|EOS|>", 
            "<|EOS|>             <|EOS|>"],


      'B': ["<|EOS|><|EOS|><|EOS|>    ", 
            "<|EOS|>           <|EOS|>", 
            "<|EOS|>           <|EOS|>", 
            "<|EOS|><|EOS|><|EOS|><   ", 
            "<|EOS|><|EOS|><|EOS|>    ", 
            "<|EOS|>           <|EOS|>", 
            "<|EOS|>           <|EOS|>", 
            "<|EOS|>           <|EOS|>", 
            "<|EOS|>           <|EOS|>", 
            "<|EOS|><|EOS|><|EOS|>    "],


      'C': ["   <|EOS|><|EOS|><|EOS|>    ", 
            "  <|EOS|>            <|EOS|>", 
            " <|EOS|>             <|EOS|>", 
            "<|EOS|>                     ", 
            "<|EOS|>                     ", 
            "<|EOS|>                     ", 
            "<|EOS|>                     ", 
            "<|EOS|>              <|EOS|>", 
            "  <|EOS|>            <|EOS|>", 
            "   <|EOS|><|EOS|><|EOS|>    "],


      'D': ["<|EOS|><|EOS|><|EOS|>     ", 
            "<|EOS|>           <|EOS|> ", 
            "<|EOS|>            <|EOS|>", 
            "<|EOS|>            <|EOS|>", 
            "<|EOS|>            <|EOS|>", 
            "<|EOS|>            <|EOS|>", 
            "<|EOS|>            <|EOS|>", 
            "<|EOS|>           <|EOS|> ", 
            "<|EOS|>           <|EOS|> ", 
            "<|EOS|><|EOS|><|EOS|>     "],


      'E': ["<|EOS|><|EOS|><|EOS|>", 
            "<|EOS|><|EOS|><|EOS|>", 
            "<|EOS|>              ", 
            "<|EOS|>              ", 
            "<|EOS|><|EOS|><|EOS|>", 
            "<|EOS|><|EOS|><|EOS|>", 
            "<|EOS|>              ", 
            "<|EOS|>              ", 
            "<|EOS|><|EOS|><|EOS|>", 
            "<|EOS|><|EOS|><|EOS|>"],


      'F': ["<|EOS|><|EOS|><|EOS|>", 
            "<|EOS|><|EOS|><|EOS|>", 
            "<|EOS|>              ", 
            "<|EOS|>              ", 
            "<|EOS|><|EOS|><|EOS|>", 
            "<|EOS|><|EOS|><|EOS|>", 
            "<|EOS|>              ", 
            "<|EOS|>              ", 
            "<|EOS|>              ", 
            "<|EOS|>              "],


      'G': ["   <|EOS|><|EOS|><|EOS|>    ", 
            "  <|EOS|>           <|EOS|> ", 
            " <|EOS|>             <|EOS|>", 
            "<|EOS|>                     ", 
            "<|EOS|>                     ",
            "<|EOS|>       <|EOS|><|EOS|>", 
            "<|EOS|>              <|EOS|>", 
            " <|EOS|>             <|EOS|>", 
            "  <|EOS|>            <|EOS|>", 
            "   <|EOS|><|EOS|><|EOS|>    "],


      'H': ["<|EOS|>              <|EOS|>", 
            "<|EOS|>              <|EOS|>", 
            "<|EOS|>              <|EOS|>", 
            "<|EOS|>              <|EOS|>", 
            "<|EOS|><|EOS|><|EOS|><|EOS|>", 
            "<|EOS|><|EOS|><|EOS|><|EOS|>", 
            "<|EOS|>              <|EOS|>", 
            "<|EOS|>              <|EOS|>", 
            "<|EOS|>              <|EOS|>", 
            "<|EOS|>              <|EOS|>"],


      'I': ["<|EOS|><|EOS|>", 
            "   <|EOS|>    ", 
            "   <|EOS|>    ", 
            "   <|EOS|>    ", 
            "   <|EOS|>    ", 
            "   <|EOS|>    ", 
            "   <|EOS|>    ", 
            "   <|EOS|>    ", 
            "   <|EOS|>    ", 
            "<|EOS|><|EOS|>"],


      'J': ["       <|EOS|><|EOS|>", 
            "              <|EOS|>", 
            "              <|EOS|>", 
            "              <|EOS|>", 
            "              <|EOS|>", 
            "              <|EOS|>", 
            "              <|EOS|>", 
            "<|EOS|>       <|EOS|>", 
            " <|EOS|>     <|EOS|> ", 
            "  <|EOS|><|EOS|>     "],


      'K': ["<|EOS|>          <|EOS|>", 
            "<|EOS|>         <|EOS|> ", 
            "<|EOS|>       <|EOS|>   ", 
            "<|EOS|>     <|EOS|>     ", 
            "<|EOS|><|EOS|>          ", 
            "<|EOS|><|EOS|>          ", 
            "<|EOS|>     <|EOS|>     ", 
            "<|EOS|>       <|EOS|>   ", 
            "<|EOS|>         <|EOS|> ", 
            "<|EOS|>          <|EOS|>"],

            
      'L': ["<|EOS|>              ", 
            "<|EOS|>              ", 
            "<|EOS|>              ", 
            "<|EOS|>              ", 
            "<|EOS|>              ", 
            "<|EOS|>              ", 
            "<|EOS|>              ", 
            "<|EOS|>              ", 
            "<|EOS|><|EOS|><|EOS|>", 
            "<|EOS|><|EOS|><|EOS|>"],


      'M': ["<|EOS|>                   <|EOS|>", 
            "<|EOS|><|EOS|>     <|EOS|><|EOS|>", 
            "<|EOS|>   <|EOS|><|EOS|>  <|EOS|>", 
            "<|EOS|>       <|EOS|>     <|EOS|>", 
            "<|EOS|>       <|EOS|>     <|EOS|>", 
            "<|EOS|>                   <|EOS|>", 
            "<|EOS|>                   <|EOS|>", 
            "<|EOS|>                   <|EOS|>", 
            "<|EOS|>                   <|EOS|>", 
            "<|EOS|>                   <|EOS|>"],


      'N': ["<|EOS|>               <|EOS|>", 
            "<|EOS|><|EOS|>        <|EOS|>", 
            "<|EOS|>   <|EOS|>     <|EOS|>", 
            "<|EOS|>     <|EOS|>   <|EOS|>", 
            "<|EOS|>      <|EOS|>  <|EOS|>", 
            "<|EOS|>       <|EOS|> <|EOS|>", 
            "<|EOS|>        <|EOS|><|EOS|>", 
            "<|EOS|>               <|EOS|>", 
            "<|EOS|>               <|EOS|>", 
            "<|EOS|>               <|EOS|>"],


      'O': ["   <|EOS|><|EOS|>     ", 
            " <|EOS|>      <|EOS|> ", 
            "<|EOS|>        <|EOS|>", 
            "<|EOS|>        <|EOS|>", 
            "<|EOS|>        <|EOS|>", 
            "<|EOS|>        <|EOS|>", 
            "<|EOS|>        <|EOS|>", 
            "<|EOS|>        <|EOS|>", 
            " <|EOS|>      <|EOS|> ", 
            "   <|EOS|><|EOS|>     "],


      'P': ["<|EOS|><|EOS|><|EOS|>  ", 
            "<|EOS|>         <|EOS|>", 
            "<|EOS|>         <|EOS|>", 
            "<|EOS|>         <|EOS|>", 
            "<|EOS|><|EOS|><|EOS|>  ", 
            "<|EOS|>                ", 
            "<|EOS|>                ", 
            "<|EOS|>                ", 
            "<|EOS|>                ", 
            "<|EOS|>                  "],

      'Q': ["  <|EOS|><|EOS|><|EOS|>   ", 
            " <|EOS|>         <|EOS|>  ", 
            "<|EOS|>           <|EOS|> ", 
            "<|EOS|>           <|EOS|> ", 
            "<|EOS|>           <|EOS|> ", 
            "<|EOS|>           <|EOS|> ", 
            "<|EOS|>           <|EOS|> ", 
            "<|EOS|>      <|EOS|>      ", 
            " <|EOS|>      <|EOS|>     ", 
            "   <|EOS|><|EOS|><|EOS|>  ",
            "                   <|EOS|>"],


      'R': ["<|EOS|><|EOS|><|EOS|>    ", 
            "<|EOS|>          <|EOS|> ", 
            "<|EOS|>          <|EOS|> ", 
            "<|EOS|>          <|EOS|> ", 
            "<|EOS|><|EOS|><|EOS|>    ", 
            "<|EOS|>     <|EOS|>      ", 
            "<|EOS|>      <|EOS|>     ", 
            "<|EOS|>       <|EOS|>    ", 
            "<|EOS|>        <|EOS|>   ", 
            "<|EOS|>         <|EOS|>  "],


      'S': ["   <|EOS|><|EOS|><|EOS|>   ", 
            "  <|EOS|>          <|EOS|> ", 
            " <|EOS|>                   ", 
            "<|EOS|>                    ", 
            "  <|EOS|><|EOS|><|EOS|>    ", 
            "                    <|EOS|>", 
            "                    <|EOS|>", 
            "                   <|EOS|> ", 
            "  <|EOS|>          <|EOS|> ", 
            "   <|EOS|><|EOS|><|EOS|>   "],


      'T': ["<|EOS|><|EOS|><|EOS|>", 
            "<|EOS|><|EOS|><|EOS|>", 
            "       <|EOS|>       ", 
            "       <|EOS|>       ", 
            "       <|EOS|>       ", 
            "       <|EOS|>       ", 
            "       <|EOS|>       ", 
            "       <|EOS|>       ", 
            "       <|EOS|>       ", 
            "       <|EOS|>       "],


      'U': ["<|EOS|>        <|EOS|>", 
            "<|EOS|>        <|EOS|>", 
            "<|EOS|>        <|EOS|>", 
            "<|EOS|>        <|EOS|>", 
            "<|EOS|>        <|EOS|>", 
            "<|EOS|>        <|EOS|>", 
            "<|EOS|>        <|EOS|>", 
            "<|EOS|>        <|EOS|>", 
            " <|EOS|>     <|EOS|> ", 
            "   <|EOS|><|EOS|>   "],


      'V': ["<|EOS|>             <|EOS|>", 
            " <|EOS|>           <|EOS|> ", 
            " <|EOS|>           <|EOS|> ", 
            "  <|EOS|>         <|EOS|>  ", 
            "  <|EOS|>         <|EOS|>  ", 
            "   <|EOS|>       <|EOS|>   ", 
            "   <|EOS|>       <|EOS|>   ", 
            "    <|EOS|>     <|EOS|>    ", 
            "     <|EOS|>   <|EOS|>     ", 
            "      <|EOS|><|EOS|>       "],


      'W': ["<|EOS|>         <|EOS|><|EOS|>         <|EOS|>", 
            " <|EOS|>       <|EOS|>  <|EOS|>       <|EOS|> ", 
            " <|EOS|>       <|EOS|>  <|EOS|>       <|EOS|> ", 
            "  <|EOS|>     <|EOS|>    <|EOS|>     <|EOS|>  ", 
            "  <|EOS|>     <|EOS|>    <|EOS|>     <|EOS|>  ", 
            "   <|EOS|>   <|EOS|>      <|EOS|>   <|EOS|>   ", 
            "   <|EOS|>   <|EOS|>      <|EOS|>   <|EOS|>   ", 
            "    <|EOS|> <|EOS|>        <|EOS|> <|EOS|>    ", 
            "    <|EOS|><|EOS|>          <|EOS|><|EOS|>    ", 
            "        <|EOS|>                <|EOS|>        "],


      'X': ["<|EOS|>         <|EOS|>", 
            " <|EOS|>       <|EOS|> ", 
            "  <|EOS|>     <|EOS|>  ", 
            "   <|EOS|>   <|EOS|>   ", 
            "    <|EOS|><|EOS|>     ", 
            "    <|EOS|><|EOS|>     ", 
            "   <|EOS|>   <|EOS|>   ", 
            "  <|EOS|>     <|EOS|>  ", 
            " <|EOS|>       <|EOS|> ", 
            "<|EOS|>         <|EOS|>"],


      'Y': ["<|EOS|>           <|EOS|>", 
            " <|EOS|>         <|EOS|> ", 
            "  <|EOS|>       <|EOS|>  ", 
            "   <|EOS|>     <|EOS|>   ", 
            "    <|EOS|>    <|EOS|>   ", 
            "     <|EOS|><|EOS|>      ", 
            "         <|EOS|>         ", 
            "         <|EOS|>         ", 
            "         <|EOS|>         ", 
            "         <|EOS|>         "],


      'Z': ["<|EOS|><|EOS|><|EOS|>", 
            "<|EOS|><|EOS|><|EOS|>", 
            "             <|EOS|> ", 
            "           <|EOS|>   ", 
            "         <|EOS|>     ", 
            "       <|EOS|>       ", 
            "     <|EOS|>         ", 
            "   <|EOS|>           ", 
            "<|EOS|><|EOS|><|EOS|>", 
            "<|EOS|><|EOS|><|EOS|>"],
      
      
      '_': ["  ", 
            "  ", 
            "  ", 
            "  ", 
            "  ", 
            "  ", 
            "  ", 
            "  ", 
            "  ", 
            "  "]
      }

      # Default pattern for unknown characters
      default_pattern = ["               ", 
                        "                ", 
                        "                ", 
                        "                ", 
                        "                ", 
                        "                ", 
                        "                ", 
                        "                ", 
                        "                ", 
                        "                "]

    # Create a list to hold the lines of the output
      output_lines = ["", "", "", "", "", "", "", "", "", ""]

      # Convert each character in the text to its <|EOS|> pattern
      for char in text.upper():
            pattern = my_patterns.get(char, default_pattern)
            for i in range(10):
                  output_lines[i] += pattern[i] + " "  # Add space between characters

      # Join the lines with newline characters
      output = "\n".join(output_lines)

      if token is None:
           return output
      else:
           return output.replace("<|EOS|>", token)

def spectial_tokens_font(text, token="<|EOS|>"):

# Define the <|EOS|> patterns for each character with a 10x10 grid
      my_patterns = {
      'A': ["          <|EOS|>          ", 
            "      <|EOS|><|EOS|>       ", 
            "     <|EOS|>   <|EOS|>     ", 
            "    <|EOS|>     <|EOS|>    ", 
            "   <|EOS|>       <|EOS|>   ", 
            "  <|EOS|><|EOS|><|EOS|>    ", 
            " <|EOS|>           <|EOS|> ", 
            "<|EOS|>             <|EOS|>", 
            "<|EOS|>             <|EOS|>", 
            "<|EOS|>             <|EOS|>"],


      'B': ["<|EOS|><|EOS|><|EOS|>    ", 
            "<|EOS|>           <|EOS|>", 
            "<|EOS|>           <|EOS|>", 
            "<|EOS|><|EOS|><|EOS|><   ", 
            "<|EOS|><|EOS|><|EOS|>    ", 
            "<|EOS|>           <|EOS|>", 
            "<|EOS|>           <|EOS|>", 
            "<|EOS|>           <|EOS|>", 
            "<|EOS|>           <|EOS|>", 
            "<|EOS|><|EOS|><|EOS|>    "],


      'C': ["   <|EOS|><|EOS|><|EOS|>    ", 
            "  <|EOS|>            <|EOS|>", 
            " <|EOS|>             <|EOS|>", 
            "<|EOS|>                     ", 
            "<|EOS|>                     ", 
            "<|EOS|>                     ", 
            "<|EOS|>                     ", 
            "<|EOS|>              <|EOS|>", 
            "  <|EOS|>            <|EOS|>", 
            "   <|EOS|><|EOS|><|EOS|>    "],


      'D': ["<|EOS|><|EOS|><|EOS|>     ", 
            "<|EOS|>           <|EOS|> ", 
            "<|EOS|>            <|EOS|>", 
            "<|EOS|>            <|EOS|>", 
            "<|EOS|>            <|EOS|>", 
            "<|EOS|>            <|EOS|>", 
            "<|EOS|>            <|EOS|>", 
            "<|EOS|>           <|EOS|> ", 
            "<|EOS|>           <|EOS|> ", 
            "<|EOS|><|EOS|><|EOS|>     "],


      'E': ["<|EOS|><|EOS|><|EOS|>", 
            "<|EOS|><|EOS|><|EOS|>", 
            "<|EOS|>              ", 
            "<|EOS|>              ", 
            "<|EOS|><|EOS|><|EOS|>", 
            "<|EOS|><|EOS|><|EOS|>", 
            "<|EOS|>              ", 
            "<|EOS|>              ", 
            "<|EOS|><|EOS|><|EOS|>", 
            "<|EOS|><|EOS|><|EOS|>"],


      'F': ["<|EOS|><|EOS|><|EOS|>", 
            "<|EOS|><|EOS|><|EOS|>", 
            "<|EOS|>              ", 
            "<|EOS|>              ", 
            "<|EOS|><|EOS|><|EOS|>", 
            "<|EOS|><|EOS|><|EOS|>", 
            "<|EOS|>              ", 
            "<|EOS|>              ", 
            "<|EOS|>              ", 
            "<|EOS|>              "],


      'G': ["   <|EOS|><|EOS|><|EOS|>    ", 
            "  <|EOS|>           <|EOS|> ", 
            " <|EOS|>             <|EOS|>", 
            "<|EOS|>                     ", 
            "<|EOS|>                     ",
            "<|EOS|>       <|EOS|><|EOS|>", 
            "<|EOS|>              <|EOS|>", 
            " <|EOS|>             <|EOS|>", 
            "  <|EOS|>            <|EOS|>", 
            "   <|EOS|><|EOS|><|EOS|>    "],


      'H': ["<|EOS|>              <|EOS|>", 
            "<|EOS|>              <|EOS|>", 
            "<|EOS|>              <|EOS|>", 
            "<|EOS|>              <|EOS|>", 
            "<|EOS|><|EOS|><|EOS|><|EOS|>", 
            "<|EOS|><|EOS|><|EOS|><|EOS|>", 
            "<|EOS|>              <|EOS|>", 
            "<|EOS|>              <|EOS|>", 
            "<|EOS|>              <|EOS|>", 
            "<|EOS|>              <|EOS|>"],


      'I': ["<|EOS|><|EOS|>", 
            "   <|EOS|>    ", 
            "   <|EOS|>    ", 
            "   <|EOS|>    ", 
            "   <|EOS|>    ", 
            "   <|EOS|>    ", 
            "   <|EOS|>    ", 
            "   <|EOS|>    ", 
            "   <|EOS|>    ", 
            "<|EOS|><|EOS|>"],


      'J': ["       <|EOS|><|EOS|>", 
            "              <|EOS|>", 
            "              <|EOS|>", 
            "              <|EOS|>", 
            "              <|EOS|>", 
            "              <|EOS|>", 
            "              <|EOS|>", 
            "<|EOS|>       <|EOS|>", 
            " <|EOS|>     <|EOS|> ", 
            "  <|EOS|><|EOS|>     "],


      'K': ["<|EOS|>          <|EOS|>", 
            "<|EOS|>         <|EOS|> ", 
            "<|EOS|>       <|EOS|>   ", 
            "<|EOS|>     <|EOS|>     ", 
            "<|EOS|><|EOS|>          ", 
            "<|EOS|><|EOS|>          ", 
            "<|EOS|>     <|EOS|>     ", 
            "<|EOS|>       <|EOS|>   ", 
            "<|EOS|>         <|EOS|> ", 
            "<|EOS|>          <|EOS|>"],

            
      'L': ["<|EOS|>              ", 
            "<|EOS|>              ", 
            "<|EOS|>              ", 
            "<|EOS|>              ", 
            "<|EOS|>              ", 
            "<|EOS|>              ", 
            "<|EOS|>              ", 
            "<|EOS|>              ", 
            "<|EOS|><|EOS|><|EOS|>", 
            "<|EOS|><|EOS|><|EOS|>"],


      'M': ["<|EOS|>                   <|EOS|>", 
            "<|EOS|><|EOS|>     <|EOS|><|EOS|>", 
            "<|EOS|>   <|EOS|><|EOS|>  <|EOS|>", 
            "<|EOS|>       <|EOS|>     <|EOS|>", 
            "<|EOS|>       <|EOS|>     <|EOS|>", 
            "<|EOS|>                   <|EOS|>", 
            "<|EOS|>                   <|EOS|>", 
            "<|EOS|>                   <|EOS|>", 
            "<|EOS|>                   <|EOS|>", 
            "<|EOS|>                   <|EOS|>"],


      'N': ["<|EOS|>               <|EOS|>", 
            "<|EOS|><|EOS|>        <|EOS|>", 
            "<|EOS|>   <|EOS|>     <|EOS|>", 
            "<|EOS|>     <|EOS|>   <|EOS|>", 
            "<|EOS|>      <|EOS|>  <|EOS|>", 
            "<|EOS|>       <|EOS|> <|EOS|>", 
            "<|EOS|>        <|EOS|><|EOS|>", 
            "<|EOS|>               <|EOS|>", 
            "<|EOS|>               <|EOS|>", 
            "<|EOS|>               <|EOS|>"],


      'O': ["   <|EOS|><|EOS|>     ", 
            " <|EOS|>      <|EOS|> ", 
            "<|EOS|>        <|EOS|>", 
            "<|EOS|>        <|EOS|>", 
            "<|EOS|>        <|EOS|>", 
            "<|EOS|>        <|EOS|>", 
            "<|EOS|>        <|EOS|>", 
            "<|EOS|>        <|EOS|>", 
            " <|EOS|>      <|EOS|> ", 
            "   <|EOS|><|EOS|>     "],


      'P': ["<|EOS|><|EOS|><|EOS|>  ", 
            "<|EOS|>         <|EOS|>", 
            "<|EOS|>         <|EOS|>", 
            "<|EOS|>         <|EOS|>", 
            "<|EOS|><|EOS|><|EOS|>  ", 
            "<|EOS|>                ", 
            "<|EOS|>                ", 
            "<|EOS|>                ", 
            "<|EOS|>                ", 
            "<|EOS|>                  "],

      'Q': ["  <|EOS|><|EOS|><|EOS|>   ", 
            " <|EOS|>         <|EOS|>  ", 
            "<|EOS|>           <|EOS|> ", 
            "<|EOS|>           <|EOS|> ", 
            "<|EOS|>           <|EOS|> ", 
            "<|EOS|>           <|EOS|> ", 
            "<|EOS|>           <|EOS|> ", 
            "<|EOS|>      <|EOS|>      ", 
            " <|EOS|>      <|EOS|>     ", 
            "   <|EOS|><|EOS|><|EOS|>  ",
            "                   <|EOS|>"],


      'R': ["<|EOS|><|EOS|><|EOS|>    ", 
            "<|EOS|>          <|EOS|> ", 
            "<|EOS|>          <|EOS|> ", 
            "<|EOS|>          <|EOS|> ", 
            "<|EOS|><|EOS|><|EOS|>    ", 
            "<|EOS|>     <|EOS|>      ", 
            "<|EOS|>      <|EOS|>     ", 
            "<|EOS|>       <|EOS|>    ", 
            "<|EOS|>        <|EOS|>   ", 
            "<|EOS|>         <|EOS|>  "],


      'S': ["   <|EOS|><|EOS|><|EOS|>   ", 
            "  <|EOS|>          <|EOS|> ", 
            " <|EOS|>                   ", 
            "<|EOS|>                    ", 
            "  <|EOS|><|EOS|><|EOS|>    ", 
            "                    <|EOS|>", 
            "                    <|EOS|>", 
            "                   <|EOS|> ", 
            "  <|EOS|>          <|EOS|> ", 
            "   <|EOS|><|EOS|><|EOS|>   "],


      'T': ["<|EOS|><|EOS|><|EOS|>", 
            "<|EOS|><|EOS|><|EOS|>", 
            "       <|EOS|>       ", 
            "       <|EOS|>       ", 
            "       <|EOS|>       ", 
            "       <|EOS|>       ", 
            "       <|EOS|>       ", 
            "       <|EOS|>       ", 
            "       <|EOS|>       ", 
            "       <|EOS|>       "],


      'U': ["<|EOS|>        <|EOS|>", 
            "<|EOS|>        <|EOS|>", 
            "<|EOS|>        <|EOS|>", 
            "<|EOS|>        <|EOS|>", 
            "<|EOS|>        <|EOS|>", 
            "<|EOS|>        <|EOS|>", 
            "<|EOS|>        <|EOS|>", 
            "<|EOS|>        <|EOS|>", 
            " <|EOS|>     <|EOS|> ", 
            "   <|EOS|><|EOS|>   "],


      'V': ["<|EOS|>             <|EOS|>", 
            " <|EOS|>           <|EOS|> ", 
            " <|EOS|>           <|EOS|> ", 
            "  <|EOS|>         <|EOS|>  ", 
            "  <|EOS|>         <|EOS|>  ", 
            "   <|EOS|>       <|EOS|>   ", 
            "   <|EOS|>       <|EOS|>   ", 
            "    <|EOS|>     <|EOS|>    ", 
            "     <|EOS|>   <|EOS|>     ", 
            "      <|EOS|><|EOS|>       "],


      'W': ["<|EOS|>         <|EOS|><|EOS|>         <|EOS|>", 
            " <|EOS|>       <|EOS|>  <|EOS|>       <|EOS|> ", 
            " <|EOS|>       <|EOS|>  <|EOS|>       <|EOS|> ", 
            "  <|EOS|>     <|EOS|>    <|EOS|>     <|EOS|>  ", 
            "  <|EOS|>     <|EOS|>    <|EOS|>     <|EOS|>  ", 
            "   <|EOS|>   <|EOS|>      <|EOS|>   <|EOS|>   ", 
            "   <|EOS|>   <|EOS|>      <|EOS|>   <|EOS|>   ", 
            "    <|EOS|> <|EOS|>        <|EOS|> <|EOS|>    ", 
            "    <|EOS|><|EOS|>          <|EOS|><|EOS|>    ", 
            "        <|EOS|>                <|EOS|>        "],


      'X': ["<|EOS|>         <|EOS|>", 
            " <|EOS|>       <|EOS|> ", 
            "  <|EOS|>     <|EOS|>  ", 
            "   <|EOS|>   <|EOS|>   ", 
            "    <|EOS|><|EOS|>     ", 
            "    <|EOS|><|EOS|>     ", 
            "   <|EOS|>   <|EOS|>   ", 
            "  <|EOS|>     <|EOS|>  ", 
            " <|EOS|>       <|EOS|> ", 
            "<|EOS|>         <|EOS|>"],


      'Y': ["<|EOS|>           <|EOS|>", 
            " <|EOS|>         <|EOS|> ", 
            "  <|EOS|>       <|EOS|>  ", 
            "   <|EOS|>     <|EOS|>   ", 
            "    <|EOS|>    <|EOS|>   ", 
            "     <|EOS|><|EOS|>      ", 
            "         <|EOS|>         ", 
            "         <|EOS|>         ", 
            "         <|EOS|>         ", 
            "         <|EOS|>         "],


      'Z': ["<|EOS|><|EOS|><|EOS|>", 
            "<|EOS|><|EOS|><|EOS|>", 
            "             <|EOS|> ", 
            "           <|EOS|>   ", 
            "         <|EOS|>     ", 
            "       <|EOS|>       ", 
            "     <|EOS|>         ", 
            "   <|EOS|>           ", 
            "<|EOS|><|EOS|><|EOS|>", 
            "<|EOS|><|EOS|><|EOS|>"],
      
      
      '_': ["  ", 
            "  ", 
            "  ", 
            "  ", 
            "  ", 
            "  ", 
            "  ", 
            "  ", 
            "  ", 
            "  "]
      }

      # Default pattern for unknown characters
      default_pattern = ["               ", 
                        "                ", 
                        "                ", 
                        "                ", 
                        "                ", 
                        "                ", 
                        "                ", 
                        "                ", 
                        "                ", 
                        "                "]

    # Create a list to hold the lines of the output
      output_lines = ["", "", "", "", "", "", "", "", "", ""]

      # Convert each character in the text to its <|EOS|> pattern
      for char in text.upper():
            pattern = my_patterns.get(char, default_pattern)
            for i in range(10):
                  output_lines[i] += pattern[i] + " "  # Add space between characters

      # Join the lines with newline characters
      output = "\n".join(output_lines)

      if token is None:
           return output
      else:
           return output.replace("<|EOS|>", token)
