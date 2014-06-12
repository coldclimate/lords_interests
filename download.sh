#!/bin/bash
for i in A B C D E F G H I J K L M N O P Q R S T U V W X Y Z; do echo ${i}; curl -o ${i}.html http://www.parliament.uk/mps-lords-and-offices/standards-and-interests/register-of-lords-interests/?letter=${i}; done
