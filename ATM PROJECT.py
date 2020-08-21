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
