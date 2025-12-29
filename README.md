simple_nn_riscv.so:     file format elf64-littleriscv


Disassembly of section .text:

0000000000000630 <deregister_tm_clones>:
     630:	0000e517          	auipc	a0,0xe
     634:	9d850513          	addi	a0,a0,-1576 # e008 <completed.0>
     638:	0000e797          	auipc	a5,0xe
     63c:	9d078793          	addi	a5,a5,-1584 # e008 <completed.0>
     640:	00a78863          	beq	a5,a0,650 <deregister_tm_clones+0x20>
     644:	0000e797          	auipc	a5,0xe
     648:	99c7b783          	ld	a5,-1636(a5) # dfe0 <_ITM_deregisterTMCloneTable@Base>
     64c:	c391                	beqz	a5,650 <deregister_tm_clones+0x20>
     64e:	8782                	jr	a5
     650:	8082                	ret

0000000000000652 <register_tm_clones>:
     652:	0000e517          	auipc	a0,0xe
     656:	9b650513          	addi	a0,a0,-1610 # e008 <completed.0>
     65a:	0000e597          	auipc	a1,0xe
     65e:	9ae58593          	addi	a1,a1,-1618 # e008 <completed.0>
     662:	8d89                	sub	a1,a1,a0
     664:	4035d793          	srai	a5,a1,0x3
     668:	91fd                	srli	a1,a1,0x3f
     66a:	95be                	add	a1,a1,a5
     66c:	8585                	srai	a1,a1,0x1
     66e:	c599                	beqz	a1,67c <register_tm_clones+0x2a>
     670:	0000e797          	auipc	a5,0xe
     674:	9787b783          	ld	a5,-1672(a5) # dfe8 <_ITM_registerTMCloneTable@Base>
     678:	c391                	beqz	a5,67c <register_tm_clones+0x2a>
     67a:	8782                	jr	a5
     67c:	8082                	ret

000000000000067e <__do_global_dtors_aux>:
     67e:	0000e797          	auipc	a5,0xe
     682:	98a7c783          	lbu	a5,-1654(a5) # e008 <completed.0>
     686:	e79d                	bnez	a5,6b4 <__do_global_dtors_aux+0x36>
     688:	1141                	addi	sp,sp,-16
     68a:	e406                	sd	ra,8(sp)
     68c:	0000e797          	auipc	a5,0xe
     690:	94c7b783          	ld	a5,-1716(a5) # dfd8 <__cxa_finalize@GLIBC_2.27>
     694:	c791                	beqz	a5,6a0 <__do_global_dtors_aux+0x22>
     696:	0000e517          	auipc	a0,0xe
     69a:	96a53503          	ld	a0,-1686(a0) # e000 <__dso_handle>
     69e:	9782                	jalr	a5
     6a0:	f91ff0ef          	jal	630 <deregister_tm_clones>
     6a4:	60a2                	ld	ra,8(sp)
     6a6:	4785                	li	a5,1
     6a8:	0000e717          	auipc	a4,0xe
     6ac:	96f70023          	sb	a5,-1696(a4) # e008 <completed.0>
     6b0:	0141                	addi	sp,sp,16
     6b2:	8082                	ret
     6b4:	8082                	ret

00000000000006b6 <frame_dummy>:
     6b6:	bf71                	j	652 <register_tm_clones>

00000000000006b8 <__tvm_ffi_add>:
     6b8:	ff010113          	addi	sp,sp,-16
     6bc:	00113423          	sd	ra,8(sp)
     6c0:	0006061b          	sext.w	a2,a2
     6c4:	00300513          	li	a0,3
     6c8:	2ea61463          	bne	a2,a0,9b0 <__tvm_ffi_add+0x2f8>
     6cc:	30058a63          	beqz	a1,9e0 <__tvm_ffi_add+0x328>
     6d0:	0005a683          	lw	a3,0(a1)
     6d4:	03f00513          	li	a0,63
     6d8:	00d54e63          	blt	a0,a3,6f4 <__tvm_ffi_add+0x3c>
     6dc:	00700613          	li	a2,7
     6e0:	24d66063          	bltu	a2,a3,920 <__tvm_ffi_add+0x268>
     6e4:	09100613          	li	a2,145
     6e8:	00d65633          	srl	a2,a2,a3
     6ec:	00167613          	andi	a2,a2,1
     6f0:	22060863          	beqz	a2,920 <__tvm_ffi_add+0x268>
     6f4:	0105a603          	lw	a2,16(a1)
     6f8:	00c54e63          	blt	a0,a2,714 <__tvm_ffi_add+0x5c>
     6fc:	00700513          	li	a0,7
     700:	24c56863          	bltu	a0,a2,950 <__tvm_ffi_add+0x298>
     704:	09100513          	li	a0,145
     708:	00c55533          	srl	a0,a0,a2
     70c:	00157513          	andi	a0,a0,1
     710:	24050063          	beqz	a0,950 <__tvm_ffi_add+0x298>
     714:	0205a503          	lw	a0,32(a1)
     718:	03f00713          	li	a4,63
     71c:	00a74e63          	blt	a4,a0,738 <__tvm_ffi_add+0x80>
     720:	00700713          	li	a4,7
     724:	24a76e63          	bltu	a4,a0,980 <__tvm_ffi_add+0x2c8>
     728:	09100713          	li	a4,145
     72c:	00a75733          	srl	a4,a4,a0
     730:	00177713          	andi	a4,a4,1
     734:	24070663          	beqz	a4,980 <__tvm_ffi_add+0x2c8>
     738:	0085b283          	ld	t0,8(a1)
     73c:	2c028a63          	beqz	t0,a10 <__tvm_ffi_add+0x358>
     740:	fba68693          	addi	a3,a3,-70
     744:	00d036b3          	snez	a3,a3
     748:	fff68693          	addi	a3,a3,-1
     74c:	0186f693          	andi	a3,a3,24
     750:	00d282b3          	add	t0,t0,a3
     754:	0102a683          	lw	a3,16(t0)
