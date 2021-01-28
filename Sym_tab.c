#include<stdio.h>
#include<conio.h>
#include<string.h>
#include<stdlib.h>

int ad=0;
struct sym_tab {
  int f;
  char label[10];
  int addr;
  struct sym_tab *next;
}s[100];

int hashin(char l[]) {
  int key=0;
  int len=strlen(l);
  for(int i=0;i<len;i++)
    key=key+((int) l[i]);
  key = key%100;
  return key;
}

void Create() {
  
  int y,key;
  char l[10];
  struct sym_tab *p;
  p=(struct sym_tab*)malloc(sizeof(struct sym_tab));
  
  do
  {
    printf("\nEnter label:");
    scanf("%s",l);
    key=hashin(l);
    
    p=&s[key];
    while((p->f)==1)
      p=p->next;
   

    strcpy(p->label,l);
    printf("\nEnter address:");
    scanf("%d",&p->addr);
    p->f=1;
    printf("\nEnter 1 to continue, 0 to stop\t:");
    scanf("%d",&y);
  } while (y==1);
}

void Insert() {

  int y,key;
  char l[10];
  struct sym_tab *p;
  p=(struct sym_tab*)malloc(sizeof(struct sym_tab));

  printf("\nEnter label:");
    scanf("%s",l);
    key=hashin(l);
    
    p=&s[key];
    while((p->f)==1)
      p=p->next;

    strcpy(p->label,l);
    printf("\nEnter address:");
    scanf("%d",&p->addr);
    p->f=1;
}

void Display() {

  int i;
  struct sym_tab *p;
  
  printf("\n\tLABEL\t\tADDRESS\n");
  for(i=0;i<100;i++)
  {
    p=&s[i];
    if((p->f)==1)
    {
      printf("\t%s\t\t%d\n",p->label,p->addr);
    }
  }
}

int Search(char l[]) {

  int key;
  key=hashin(l);
  struct sym_tab *p;
  p=&s[key];

  while((p->f)==1)
  {
    if(strcmp(p->label,l)==0)
      {
        ad=p->addr;
        return 1;
      }
    p=p->next;
  }
  return 0;
}

void Modify() {

  int key;
  char l[10];
  struct sym_tab *p;

  printf("\nEnter label to be modified:");
  scanf("%s",l);
  key=hashin(l);
  p=&s[key];

  while((p->f)==1)
  {
    if(strcmp(p->label,l)==0)
    {
      printf("\nEnter new address:");
      scanf("%d",&p->addr);
      break;
    }
    else
      p=p->next;
  }
}

void symbol() {
  
  int op,y=0;

  char la[10];
  
  do
  {
    printf("\n\tSYMBOL TABLE IMPLEMENTATION\n");
    printf("\n\t0.CREATE\n\t1.INSERT\n\t2.DISPLAY\n\t3.SEARCH\n\t4.MODIFY\n\t5.END\n");
    printf("\n\tEnter your option : ");
    scanf("%d",&op);
    switch(op)
    {
      case 0:Create();
             break;
      case 1:Insert();
             break;
      case 2:Display();
             break;
      case 3:printf("\n\tEnter the label to be searched : ");
             scanf("%s",la);
             y=Search(la);
             printf("\n\tSearch Result:");
             if(y==1)
              printf("\n\tThe label is present in the symbol table with address: %d\n",ad);
             else
              printf("\n\tThe label is not present in the symbol table\n");
             break;
      case 4:Modify();
             break;
      case 5:exit(0);
      default:printf("\n\tINVALID INPUT!!");
    }
  }while(op<6);
}

void main() {
  symbol();
  getch();
}