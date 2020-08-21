print("""
       *       * * * * * *     *         *        *         *       *         * * * *    *       *    * * *    *        *   * * * * *
      * *           *          * *     * *        * *     * *      * *       *           *       *      *      * *      *   *
     *   *          *          *  *   *  *        *  *   *  *     *   *      *           *       *      *      *  *     *   *
    *     *         *          *   * *   *        *   * *   *    *     *     *           * * * * *      *      *   *    *   * * * * *
   * * * * *        *          *    *    *        *    *    *   * * * * *    *           *       *      *      *    *   *   *
  *         *       *          *         *        *         *  *         *   *           *       *      *      *     *  *   * 
 *           *      *          *         *        *         * *           *   * * * *    *       *    * * *    *      * *   * * * * *
Published by:
     Harpreet Kaur

                                                                                                                                                               """)
try:
    
    f = open('Accounts.txt', 'r')
    f.close()
except FileNotFoundError:
    f = open('Accounts.txt', 'w')
    f.close()
'-----------------------------------------------'
import os
import time
def clear_screen()
os.system('clear')
print()
def read_file(file_name):
    opened_file=open(file_name,'r')
    lines_list=[]
    for line in opened_file:
        line=line.split()
        lines_list.append(line)
    return lines_list
def print_process(process):
    date='{}'.format(process[2:7])
    print('{0}\t{1}\t{2}{3: ^10}'.format(
        process[0],
        process[1].center(len('change_password')),
        date.center(len(date)),
        process[7],
        process[8]
        )
        )

    

