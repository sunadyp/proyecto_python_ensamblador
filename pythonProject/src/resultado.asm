.data
    y: .word 0
    x: .word 0
    T2: .word 0
    T4: .word 0
    T5: .word 0
    T3: .word 0
    T1: .word 0
    str_1: .asciiz "Iniciando ciclo"
    str_2: .asciiz "El valor objetivo es:"
    str_3: .asciiz "Fin del programa"

.text
main:
    # (=, 0, None, x)
    li $t0, 0
    sw $t0, x
    # (=, 30, None, T1)
    li $t0, 30
    sw $t0, T1
    # (=, 15, None, T2)
    li $t0, 15
    sw $t0, T2
    # (=, 15, None, y)
    li $t0, 15
    sw $t0, y
    # (PRINT, "Iniciando ciclo", None, None)
    li $v0, 4
    la $a0, str_1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    # (LABEL, None, None, L1)
L1:
    # (<, x, y, T3)
    lw $t0, x
    lw $t1, y
    slt $t2, $t0, $t1
    sw $t2, T3
    # (IF_FALSE, T3, None, L2)
    lw $t0, T3
    beqz $t0, L2
    # (+, x, 5, T4)
    lw $t0, x
    li $t1, 5
    add $t2, $t0, $t1
    sw $t2, T4
    # (=, T4, None, x)
    lw $t0, T4
    sw $t0, x
    # (==, x, 15, T5)
    lw $t0, x
    li $t1, 15
    seq $t2, $t0, $t1
    sw $t2, T5
    # (IF_FALSE, T5, None, L3)
    lw $t0, T5
    beqz $t0, L3
    # (PRINT, "El valor objetivo es:", None, None)
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
    # (LABEL, None, None, L3)
L3:
    # (GOTO, None, None, L1)
    j L1
    # (LABEL, None, None, L2)
L2:
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
