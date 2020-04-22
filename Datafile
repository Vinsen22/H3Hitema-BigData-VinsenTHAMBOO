FROM ubuntu:18.04
ENV TZ=Europe/Minsk
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN mkdir /workspace
WORKDIR /workspace
COPY . ./workspace
RUN apt update
RUN apt install sudo -y
RUN sudo apt install python3 -y
RUN sudo apt install jupyter-notebook -y
RUN sudo apt install git -y
RUN sudo apt install python3-pip -y
EXPOSE 8000
