.data
    a: .word 0
    T2: .word 0
    b: .word 0
    T3: .word 0
    res1: .word 0
    res2: .word 0
    T4: .word 0
    c: .word 0
    T1: .word 0

.text
main:
    # (=, 10, None, a)
    li $t0, 10
    sw $t0, a
    # (=, 20, None, b)
    li $t0, 20
    sw $t0, b
    # (=, 5, None, c)
    li $t0, 5
    sw $t0, c
    # (*, b, c, T1)
    lw $t0, b
    lw $t1, c
    mul $t2, $t0, $t1
    sw $t2, T1
    # (+, a, T1, T2)
    lw $t0, a
    lw $t1, T1
    add $t2, $t0, $t1
    sw $t2, T2
    # (=, T2, None, res1)
    lw $t0, T2
    sw $t0, res1
    # (+, a, b, T3)
    lw $t0, a
    lw $t1, b
    add $t2, $t0, $t1
    sw $t2, T3
    # (*, T3, c, T4)
    lw $t0, T3
    lw $t1, c
    mul $t2, $t0, $t1
    sw $t2, T4
    # (=, T4, None, res2)
    lw $t0, T4
    sw $t0, res2
    # (PRINT, res1, None, None)
    li $v0, 1
    lw $a0, res1
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    # (PRINT, res2, None, None)
    li $v0, 1
    lw $a0, res2
    syscall
    li $a0, 10
    li $v0, 11
    syscall

    # Fin del programa
    li $v0, 10
    syscall
