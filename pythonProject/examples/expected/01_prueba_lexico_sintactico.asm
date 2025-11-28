.data
    x: .word 0
    T1: .word 0

.text
main:
    # (=, 100, None, x)
    li $t0, 100
    sw $t0, x
    # (>, x, 0, T1)
    lw $t0, x
    li $t1, 0
    sgt $t2, $t0, $t1
    sw $t2, T1
    # (IF_FALSE, T1, None, L1)
    lw $t0, T1
    beqz $t0, L1
    # (PRINT, x, None, None)
    li $v0, 1
    lw $a0, x
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    # (GOTO, None, None, L2)
    j L2
    # (LABEL, None, None, L1)
L1:
    # (PRINT, 0, None, None)
    li $v0, 1
    li $a0, 0
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    # (LABEL, None, None, L2)
L2:

    # Fin del programa
    li $v0, 10
    syscall
