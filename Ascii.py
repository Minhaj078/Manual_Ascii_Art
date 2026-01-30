def generate_ascii_img():
    height = 28
    width = 56

    for row in range(height):
        for col in range(width):
            char = ' '

            if row == 0:
                if 0 <= col <= 55:
                    char = "."

            elif row == 1:
                if 0 <= col <= 18:
                    char = "."
                elif 19<= col <= 26:
                    char = ":"
                elif 27 <= col <= 29:
                    char = "*"
                elif 30 <= col <= 31:
                    char = ":"
                elif 32 <= col <= 55:
                    char = "."
            
            elif row == 2:
                if 0 <= col <= 15:
                    char = "."
                elif 16 <= col <= 17:
                    char = ":"
                elif 18 <= col <= 20:
                    char = "*"
                elif 21 <= col <= 30:
                    char = "#"
                elif col == 31:
                    char = "*"
                elif 32 <= col <= 33:
                    char = ":"
                elif 34 <= col <= 55:
                    char = "."

            elif row == 3:
                if 0 <= col <= 14:
                    char = "."
                elif 15 <= col <= 16:
                    char = "*"
                elif 17 <= col <= 22:
                    char = "#"
                elif 23 <= col <= 24:
                    char = "*"
                elif 25 <= col <= 30:
                    char = ":"
                elif 31 <= col <= 33:
                    char = "*"
                elif 34 <= col <= 35:
                    char = ":"
                elif 36 <= col <= 55:
                    char = "."

            elif row == 4:
                if 0 <= col <= 13:
                    char = "." 
                elif col == 14:
                    char = "*"
                elif 15 <= col <= 20:
                    char = "#"
                elif 21 <= col <= 23:
                    char = "*"
                elif 24 <= col <= 33:
                    char = ":"
                elif 34 <= col <= 35:
                    char = "*"
                elif col == 36:
                    char = ":"
                elif 37 <= col <= 55:
                    char = "."

            elif row == 5:
                if 0 <= col <= 12:
                    char = "."
                elif col == 13:
                    char = ":"
                elif 14 <= col <= 15:
                    char = "#"
                elif 16 <= col <= 23:
                    char = "*"
                elif 24 <= col <= 34:
                    char = ":"
                elif 35 <= col <= 36:
                    char = "*"
                elif col == 37:
                    char = ":"
                elif 38 <= col <= 55:
                    char = "."
            
            elif row == 6:
                if 0 <= col <= 12:
                    char = "."
                elif col == 13:
                    char = ":"
                elif 14 <= col <= 15:
                    char = "#"
                elif 16 <= col <= 23:
                    char = "*"
                elif 24 <= col <= 35:
                    char = ":"
                elif 36 <= col <= 37:
                    char = "*"
                elif col == 37:
                    char = ":"
                elif 38 <= col <= 55:
                    char = "."

            elif row == 7:
                if 0 <= col <= 13:
                    char = "."
                elif col == 14:
                    char = "*"
                elif 15 <= col <= 21:
                    char = "#"
                elif 22 <= col <= 31:
                    char = "*"
                elif 32 <= col <= 35:
                    char = ":"
                elif 36 <= col <= 37:
                    char = "*"
                elif 38 <= col <= 55:
                    char = "."
            elif row == 8:
                if 0 <= col <= 12:
                    char = "."
                elif col == 13:
                    char = ":"
                elif 14 <= col <= 18:
                    char = "#"
                elif 19 <= col <= 27:
                    char = "*"
                elif 28 <= col <= 29:
                    char = ":"
                elif 30 <= col <= 31:
                    char = "*"
                elif 32 <= col <= 35:
                    char = ":"
                elif col == 36:
                    char = "*"
                elif col == 37:
                    char = ":"
                elif 38 <= col <= 55:
                    char = "."
            elif row == 9:
                if 0 <= col <= 12:
                    char = "."
                elif col == 13:
                    char = ":"
                elif 14 <= col <= 18:
                    char = "#"
                elif 19 <= col <= 20:
                    char = "*"
                elif 21 <= col <= 23:
                    char = ":"
                elif 24 <= col <= 26:
                    char = "*"
                elif 27 <= col <= 36:
                    char = ":"
                elif 37 <= col <= 55:
                    char = "."
            
            elif row == 10:
                if 0 <= col <= 13:
                    char = "."
                elif col == 14:
                    char = "*"
                elif 15 <= col <= 18:
                    char = "#"
                elif 19 <= col <= 28:
                    char = "*"
                elif 29 <= col <= 31:
                    char = ":"
                elif col == 32:
                    char = "*"
                elif 33 <= col <= 36:
                    char = ":"
                elif 37 <= col <= 55:
                    char = "."

            elif row == 11:
                if 0 <= col <= 14:
                    char = "."
                elif col == 15:
                    char = ":"
                elif col == 16:
                    char = "*"
                elif 17 <= col <= 18:
                    char = "#"
                elif 19 <= col <= 23:
                    char = "*"
                elif col == 24:
                    char = "#"
                elif 25 <= col <= 28:
                    char = "*"
                elif 29 <= col <= 30:
                    char = "*"
                elif 31 <= col <= 33:
                    char = ":"
                elif 34 <= col <= 55:
                    char = "."

            elif row == 12:
                if 0 <= col <= 14:
                    char = "."
                elif col == 15:
                    char = ":"
                elif 16 <= col <= 19:
                    char = "#"
                elif 20 <= col <= 27:
                    char = "*"
                elif 28 <= col <= 35:
                    char = ":"
                elif 26 <= col <= 55:
                    char = "."

            elif row == 13:
                if 0 <= col <= 13:
                    char = "."
                elif col == 14:
                    char = "#"
                elif 15 <= col <= 17:
                    char = "@"
                elif 18 <= col <= 22:
                    char = "#"
                elif 23 <= col <= 24:
                    char = "*"
                elif 25 <= col <= 33:
                    char = ":"
                elif 34 <= col <= 55:
                    char = "."

            elif row == 14:
                if 0 <= col <= 13:
                    char = "."
                elif col == 14:
                    char = ":"
                elif col == 15:
                    char = "#"
                elif 16 <= col <= 20:
                    char = "@"
                elif 21 <= col <= 26:
                    char = "#"
                elif 27 <= col <= 32:
                    char = "*"
                elif col == 33:
                    char = "#"
                elif 34 <= col <= 35:
                    char = ":"
                elif 36 <= col <= 55:
                    char = "."

            elif row == 15:
                if 0 <= col <= 11:
                    char = "."
                elif col == 12:
                    char = "*"
                elif col == 13:
                    char = "#"
                elif 14 <= col <= 21:
                    char = "@"
                elif 22 <= col <= 29:
                    char = "#"
                elif 30 <= col <= 32:
                    char = "*"
                elif 33 <= col <= 34:
                    char = "@"
                elif 35 <= col <= 39:
                    char = "#"
                elif col == 40:
                    char = "*"
                elif 41 <= col <= 42:
                    char = ":"
                elif 43 <= col <= 55:
                    char = "."

            elif row == 16:
                if 0 <= col <= 8:
                    char = "."
                elif col == 9:
                    char = ":"
                elif col == 10:
                    char = "*"
                elif 11 <= col <= 12:
                    char = '#' 
                elif 13 <= col <= 23:
                    char = "@"
                elif col == 24:
                    char = "#"
                elif 25 <= col <= 30:
                    char = "*"
                elif col == 31:
                    char = ":"
                elif col == 32:
                    char = "#"
                elif 33 <= col <= 35:
                    char = "@"
                elif 36 <= col <= 40:
                    char = "#"
                elif col == 41:
                    char = "@"
                elif 42 <= col <= 43:
                    char = "#"
                elif col == 44:
                    char = "*"
                elif 45 <= col <= 55:
                    char = "."

            elif row == 17:
                if 0 <= col <= 5:
                    char = "."
                elif col == 6:
                    char = "*"
                elif col == 7:
                    char = "#"
                elif col == 8:
                    char = "@"
                elif 9 <= col <=12:
                    char = "#"
                elif 13 <= col <= 24:
                    char = "@"
                elif 25 <= col <= 26:
                    char = "#"
                elif 27 <= col <= 28:
                    char = "*"
                elif 29 <= col <= 31:
                    char = "#"
                elif 32 <= col <= 36:
                    char = "@"
                elif 37 <= col <= 45:
                    char = "#"
                elif col == 46:
                    char = ":"
                elif 47 <= col <= 55:
                    char = "."

            elif row == 18:
                if 0<= col <= 2:
                    char = "."
                elif col == 3:
                    char = ":"
                elif col == 4:
                    char = "#"
                elif 5 <= col <= 7:
                    char = "@"
                elif 8 <= col <= 13:
                    char = "#"
                elif col == 14:
                    char = "@"
                elif col == 15:
                    char = "#"
                elif 16 <= col <= 21:
                    char = "@"
                elif 22 <= col <= 23:
                    char = "#"
                elif 24 <= col <= 37:
                    char = "@"
                elif col == 38:
                    char = "#"
                elif 39 <= col <= 40:
                    char = "@"
                elif 41 <= col <= 45:
                    char = "#"
                elif col == 46:
                    char = "*"
                elif 47 <= col <= 55:
                    char = "."

            elif row == 19:
                if 0 <= col <= 1:
                    char = "."
                elif col == 2:
                    char = "#"
                elif 3 <= col <= 8:
                    char = "@"
                elif 9 <= col <= 16:
                    char = "#"
                elif 17 <= col <= 20:
                    char = "@"
                elif 21 <= col <= 26:
                    char = "#"
                elif 27 <= col <= 40:
                    char = "@"
                elif 41 <= col <= 42:
                    char = "#"
                elif 43 <= col <= 44:
                    char = "@"
                elif col == 45:
                    char = "#"
                elif col == 46:
                    char = "@"
                elif col == 47:
                    char = "#"
                elif 48 <= col <= 55:
                    char = "."   
            
            elif row == 20:
                if col == 0:
                    char = "."
                elif 1 <= col <= 10:
                    char = "@"
                elif 11 <= col <= 13:
                    char = "#"
                elif 14 <= col <= 15:
                    char = "@"
                elif 16 <= col <= 17:
                    char = "#"
                elif 18 <= col <= 20:
                    char = "@"
                elif 21 <= col <= 25:
                    char = "#"
                elif 26 <= col <= 40:
                    char = "@"
                elif 41 <= col <= 43:
                    char = "#"
                elif 44 <= col <= 46:
                    char = "@"
                elif 47 <= col <= 48:
                    char = "#"
                elif col == 49:
                    char = "*"
                elif 50 <= col <= 55:
                    char = "."

            elif row == 21:
                if col == 0:
                    char = "#"
                elif 1 <= col <= 8:
                    char = "@"
                elif 9 <= col <= 10:
                    char = "#"
                elif 11 <= col <= 12:
                    char = "@"
                elif 13 <= col <= 14:
                    char = "#"
                elif 15 <= col <= 16:
                    char = "@"
                elif 17 <= col <= 18:
                    char = "#"
                elif 19 <= col <= 21:
                    char = "@"
                elif 22 <= col <= 24:
                    char = "#"
                elif 25 <= col <= 40:
                    char = "@"
                elif 41 <= col <= 44:
                    char = "#"
                elif 45 <= col <= 46:
                    char = "@"
                elif col == 47:
                    char = "#"
                elif 48 <= col <= 49:
                    char = "@"
                elif col == 50:
                    char = "#"
                elif 51 <= col <= 55:
                    char = "."
            
            elif row == 22:
                if 0 <= col <= 9:
                    char = "@"
                elif 10 <= col <= 12:
                    char = "#"
                elif 13 <= col <= 19:
                    char = "@"
                elif 18 <= col <= 19:
                    char = "#"
                elif 20 <= col <= 21:
                    char = "@"
                elif 22 <= col <= 27:
                    char = "#"
                elif 28 <= col <= 38:
                    char = "@"
                elif 39 <= col <= 41:
                    char = "#"
                elif 42 <= col <= 50:
                    char = "@"
                elif col == 51:
                    char = "#"
                elif 52 <= col <= 55:
                    char = "."

            elif row == 23:
                if 0 <= col <= 5:
                    char = "@"
                elif col == 6:
                    char = "#"
                elif 7 <= col <= 10:
                    char = "@"
                elif col == 11:
                    char = "#"
                elif col == 12:
                    char = "@"
                elif col == 13:
                    char = "#"
                elif 14 <= col <= 17:
                    char = "@"
                elif 18 <= col <= 19:
                    char = "#"
                elif 20 <= col <= 21:
                    char = "@"
                elif 22 <= col <= 31:
                    char = "#"
                elif 32 <=col <= 40:
                    char = "@"
                elif 41 <= col <= 42:
                    char = "#"
                elif 43 <= col <= 49:
                    char = "@"
                elif col == 50:
                    char = "#"
                elif col == 51:
                    char = "@"
                elif col == 52:
                    char = "#"
                elif col == 52:
                    char = "*"
                elif 52 <= col <= 55:
                    char = "."

            elif row == 24:
                if 0 <= col <= 5:
                    char = "@"
                elif 6<= col <= 7:
                    char = "#"
                elif 8 <= col <= 18:
                    char = "@"
                elif col == 19:
                    char = "#"
                elif 20 <= col <= 21:
                    char = "@"
                elif 22 <= col <= 32:
                    char = "#"
                elif 33 <= col <= 41:
                    char = "@"
                elif col == 42:
                    char = "#"
                elif 43 <= col <= 49:
                    char = "@"
                elif 50 <= col <= 51:
                    char = "#"
                elif 52 <= col <= 53:
                    char = "@"
                elif 54 <= col <= 55:
                    char = "."
            
            elif row == 25:
                if 0 <= col <= 6:
                    char = "@"
                elif 7 <= col<= 8:
                    char = "#"
                elif 9 <= col <= 18:
                    char = "@"
                elif col == 19:
                    char = "#"
                elif col == 20:
                    char = "@"
                elif 21 <= col <= 23:
                    char = "#"
                elif 24 <= col <= 25:
                    char = "@"
                elif 26 <= col <= 28:
                    char = "#"
                elif col == 29:
                    char = "@"
                elif 30 <= col <= 32:
                    char = "#"
                elif 33 <= col <= 53:
                    char = "@"
                elif col == 54:
                    char = "*"
                elif col == 55:
                    char= "."
            
            elif row == 26:
                if 0 <= col <= 9:
                    char = "@"
                elif col == 10:
                    char = "#"
                elif 11 <= col <= 22:
                    char = "@"
                elif col == 23:
                    char = "#"
                elif 24 <= col <= 27:
                    char = "@"
                elif col == 28:
                    char = "#"
                elif col == 29:
                    char = "@"
                elif 30 <= col <= 33:
                    char = "#"
                elif 34 <= col <= 54:
                    char = "@"
                elif col == 55:
                    char = "#"

            elif row == 27:
                if 0 <= col <= 10:
                    char = "@"
                elif col == 11:
                    char = "#"
                elif 12 <= col <= 27:
                    char = "@"
                elif col == 28:
                    char = "#"
                elif 29 <= col <= 30:
                    char = "@"
                elif 31 <= col <= 34:
                    char = "#"
                elif 35 <= col <= 53:
                    char = "@"
                elif col == 54:
                    char = "#"
                elif col == 55:
                    char = "@"

            print(char, end = '')
        print()

generate_ascii_img()

