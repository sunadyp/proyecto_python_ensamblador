.data
    total: .word 0
    T2: .word 0
    T3: .word 0
    contador: .word 0
    limite: .word 0
    T4: .word 0
    T1: .word 0

.text
main:
    # (=, 0, None, total)
    li $t0, 0
    sw $t0, total
    # (=, 1, None, contador)
    li $t0, 1
    sw $t0, contador
    # (=, 11, None, limite)
    li $t0, 11
    sw $t0, limite
    # (LABEL, None, None, L1)
L1:
    # (<, contador, limite, T1)
    lw $t0, contador
    lw $t1, limite
    slt $t2, $t0, $t1
    sw $t2, T1
    # (IF_FALSE, T1, None, L2)
    lw $t0, T1
    beqz $t0, L2
    # (+, total, contador, T2)
    lw $t0, total
    lw $t1, contador
    add $t2, $t0, $t1
    sw $t2, T2
    # (=, T2, None, total)
    lw $t0, T2
    sw $t0, total
    # (+, contador, 1, T3)
    lw $t0, contador
    li $t1, 1
    add $t2, $t0, $t1
    sw $t2, T3
    # (=, T3, None, contador)
    lw $t0, T3
    sw $t0, contador
    # (==, contador, 5, T4)
    lw $t0, contador
    li $t1, 5
    seq $t2, $t0, $t1
    sw $t2, T4
    # (IF_FALSE, T4, None, L3)
    lw $t0, T4
    beqz $t0, L3
    # (PRINT, total, None, None)
    li $v0, 1
    lw $a0, total
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
    # (PRINT, total, None, None)
    li $v0, 1
    lw $a0, total
    syscall
    li $a0, 10
    li $v0, 11
    syscall

    # Fin del programa
    li $v0, 10
    syscall
