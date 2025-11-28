.data
    a: .word 0

.text
main:
    # (=, 10, None, a)
    li $t0, 10
    sw $t0, a
    # (=, 5, None, a)
    li $t0, 5
    sw $t0, a
    # (PRINT, a, None, None)
    li $v0, 1
    lw $a0, a
    syscall
    li $a0, 10
    li $v0, 11
    syscall
    # (PRINT, a, None, None)
    li $v0, 1
    lw $a0, a
    syscall
    li $a0, 10
    li $v0, 11
    syscall

    # Fin del programa
    li $v0, 10
    syscall
