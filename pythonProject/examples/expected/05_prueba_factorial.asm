.data
    numero: .word 0
    T2: .word 0
    T3: .word 0
    res: .word 0
    T1: .word 0

.text
main:
    # (=, 5, None, numero)
    li $t0, 5
    sw $t0, numero
    # (=, 1, None, res)
    li $t0, 1
    sw $t0, res
    # (LABEL, None, None, L1)
L1:
    # (>, numero, 1, T1)
    lw $t0, numero
    li $t1, 1
    sgt $t2, $t0, $t1
    sw $t2, T1
    # (IF_FALSE, T1, None, L2)
    lw $t0, T1
    beqz $t0, L2
    # (*, res, numero, T2)
    lw $t0, res
    lw $t1, numero
    mul $t2, $t0, $t1
    sw $t2, T2
    # (=, T2, None, res)
    lw $t0, T2
    sw $t0, res
    # (-, numero, 1, T3)
    lw $t0, numero
    li $t1, 1
    sub $t2, $t0, $t1
    sw $t2, T3
    # (=, T3, None, numero)
    lw $t0, T3
    sw $t0, numero
    # (GOTO, None, None, L1)
    j L1
    # (LABEL, None, None, L2)
L2:
    # (PRINT, res, None, None)
    li $v0, 1
    lw $a0, res
    syscall
    li $a0, 10
    li $v0, 11
    syscall

    # Fin del programa
    li $v0, 10
    syscall
