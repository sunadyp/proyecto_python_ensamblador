.data
    x: .word 0
    T1: .word 0
    str_1: .asciiz "Inicio del programa"
    str_2: .asciiz "El numero es mayor a 5"
    str_3: .asciiz "Fin del programa"

.text
main:
    # (PRINT, "Inicio del programa", None, None)
    li $v0, 4
    la $a0, str_1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    # (=, 10, None, x)
    li $t0, 10
    sw $t0, x
    # (>, x, 5, T1)
    lw $t0, x
    li $t1, 5
    sgt $t2, $t0, $t1
    sw $t2, T1
    # (IF_FALSE, T1, None, L1)
    lw $t0, T1
    beqz $t0, L1
    # (PRINT, "El numero es mayor a 5", None, None)
    li $v0, 4
    la $a0, str_2
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    # (PRINT, x, None, None)
    li $v0, 1
    lw $a0, x
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    # (LABEL, None, None, L1)
L1:
    # (PRINT, "Fin del programa", None, None)
    li $v0, 4
    la $a0, str_3
    syscall
    li $a0, 10
    li $v0, 11
    syscall

    # Fin del programa
    li $v0, 10
    syscall
