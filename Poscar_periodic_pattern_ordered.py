import math

# Basic parameters
a = 3.19
b = 3.19
c = 14.874
# Params
num_lattice = 30
rec_name = "POSCAR_pattern_ordered_mini"
start = (15, 15)
size = 9
#
#
pos_Mo = []
pos_S = []
step = 1 / num_lattice

num_Mo = 0
num_S = 0
lattice_a = a * num_lattice
lattice_b = b * num_lattice
lattice_c = c

base_Mo1 = [1 / 3, 2 / 3, 0.25]
base_Mo2 = [2 / 3, 1 / 3, 0.75]
base_S1 = [2 / 3, 1 / 3, 0.355174]
base_S2 = [1 / 3, 2 / 3, 0.855174]
base_S3 = [2 / 3, 1 / 3, 0.144826]
base_S4 = [1 / 3, 2 / 3, 0.644826]

defect = []
for i in range(0, size):
    for j in range(0, size):
        defect.append((i + start[0], j + start[1]))
        defect.append((-i + start[0], -j + start[1]))
    for j in range(0, size - i):
        defect.append((i + start[0], -j + start[1]))
        defect.append((-i + start[0], j + start[1]))

for i in range(num_lattice):
    for j in range(num_lattice):
        if (i, j) in defect:
            check = False
        else:
            check = True

        if check:
            pos_Mo.append(
                [
                    base_Mo1[0] / num_lattice + step * i,
                    base_Mo1[1] / num_lattice + step * j,
                    base_Mo1[2],
                ]
            )
            pos_Mo.append(
                [
                    base_Mo2[0] / num_lattice + step * i,
                    base_Mo2[1] / num_lattice + step * j,
                    base_Mo2[2],
                ]
            )
            num_Mo += 2

            pos_S.append(
                [
                    base_S1[0] / num_lattice + step * i,
                    base_S1[1] / num_lattice + step * j,
                    base_S1[2],
                ]
            )
            num_S += 1

            pos_S.append(
                [
                    base_S2[0] / num_lattice + step * i,
                    base_S2[1] / num_lattice + step * j,
                    base_S2[2],
                ]
            )
            num_S += 1

            pos_S.append(
                [
                    base_S3[0] / num_lattice + step * i,
                    base_S3[1] / num_lattice + step * j,
                    base_S3[2],
                ]
            )
            num_S += 1

            pos_S.append(
                [
                    base_S4[0] / num_lattice + step * i,
                    base_S4[1] / num_lattice + step * j,
                    base_S4[2],
                ]
            )
            num_S += 1


# Poscar
file_data = open(rec_name, "w")
file_data.write(rec_name + "\n")
file_data.write(str(num_lattice) + "\n")


file_data.write(str(lattice_a) + "\t" + str(0) + "\t" + str(0) + "\n")
file_data.write(
    str(-lattice_b / 2)
    + "\t"
    + str(lattice_b * math.sqrt(3) / 2)
    + "\t"
    + str(0)
    + "\n"
)
file_data.write(str(0) + "\t" + str(0) + "\t" + str(lattice_c) + "\n")
file_data.write("Mo" + "\t" + "S" + "\n")
file_data.write(str(num_Mo) + "\t" + str(num_S) + "\n")
file_data.write("Direct" + "\n")
for Mo_pos in pos_Mo:
    file_data.write(
        str(Mo_pos[0]) + "\t" + str(Mo_pos[1]) + "\t" + str(Mo_pos[2]) + "\n"
    )
for S_pos in pos_S:
    file_data.write(str(S_pos[0]) + "\t" + str(S_pos[1]) + "\t" + str(S_pos[2]) + "\n")
file_data.close()
