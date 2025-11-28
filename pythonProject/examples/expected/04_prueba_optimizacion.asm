.data
    resultado: .word 0
    T1: .word 0
    T2: .word 0

.text
main:
    # (=, 30, None, T1)
    li $t0, 30
    sw $t0, T1
    # (=, 60, None, T2)
    li $t0, 60
    sw $t0, T2
    # (=, 60, None, resultado)
    li $t0, 60
    sw $t0, resultado
    # (PRINT, resultado, None, None)
    li $v0, 1
    lw $a0, resultado
    syscall
    li $a0, 10
    li $v0, 11
    syscall

    # Fin del programa
    li $v0, 10
    syscall
