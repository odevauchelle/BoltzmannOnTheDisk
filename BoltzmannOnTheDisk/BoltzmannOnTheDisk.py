from scipy.special import iv
from numpy import linspace, trapz, pi, array, vectorize

def I(z) :
    '''
    Modified Bessel function of the first kind of order 0.
    '''
    return iv(0,z)

def Z( a, r = None ) :

    '''
    Partition function for the Boltzmann distribution on the unit disk.
            / /
    Z(a) =  | | exp( a*y ) dx dy
            / /
           disk
    '''

    if r is None :
        r = linspace(0,1,300)

    if a == 0 :
        return 0
    else :
        return 2*pi*trapz( I( a*r )*r , r )

def d_log_Z( a, r = None ) :

    '''
    Average position for the Boltzmann distribution on the unit disk.

    <y> = ( dZ/da )/Z

    with

            / /
    Z(a) =  | | exp( a*y ) dx dy
            / /
           disk
    '''

    if a == 0 :
        return 0
    else :
        return -2/a + 2*pi*I(a)/( Z( a, r )*a )


Z = vectorize(Z)
d_log_Z = vectorize(d_log_Z)

if __name__ == '__main__' :

    from pylab import *

    print(Z(3))

    a = linspace(-1,1,51)*25

    plot( a, d_log_Z(a) )

    a = linspace( 5, max(a), 30 )
    plot( a, 1 - 3/(2*a), '--', label = r'$1 - \dfrac{3}{2a}$' )


    a = array( [-1,1] )*2
    plot( a, a/4, '--', label = r'$\dfrac{a}{4}$' )

    legend()
    xlabel('$a$')
    ylabel(r"$\langle y\rangle = Z_a'/Z_a$")

    # savefig('../Z.svg', bbox_inches = 'tight')

    show()
