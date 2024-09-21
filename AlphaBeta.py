def alpha_complement(alpha):
    return ''.join(['0' if bit == '1' else '1' for bit in alpha])

def beta_complement(alpha):
    alpha_comp = alpha_complement(alpha)
    beta = list(alpha_comp)
    
    for i in range(len(alpha_comp) - 1, -1, -1):
        if alpha_comp[i] == '0':
            beta[i] = '1'
            break
        beta[i] = '0'
    
    return ''.join(beta)

alpha = "1010101"
alpha_comp = alpha_complement(alpha)
beta_comp = beta_complement(alpha)

print("Alpha complement:", alpha_comp)
print("Beta complement:", beta_comp)
