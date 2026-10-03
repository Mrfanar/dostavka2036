S='/tmp/claude-0/-home-claude/9b1d3969-b347-5727-adb6-d6b9273783fd/scratchpad/'
s=open(S+'index_pre_guard.html').read()
a="  build(){return vao(new Float32Array(P),new Int8Array(N),new Uint8Array(C))}};\n return o}"
assert a in s
s=s.replace(a,"""  raw(){return[P,N,C]},
  cat(q){const[a,b,c]=q.raw();for(let i=0;i<a.length;i++){P.push(a[i]);N.push(b[i]);C.push(c[i])}return o},
  ry(a){const c=Math.cos(a),s=Math.sin(a);for(let i=0;i<P.length;i+=3){const x=P[i],z=P[i+2];P[i]=x*c+z*s;P[i+2]=-x*s+z*c;const nx=N[i],nz=N[i+2];N[i]=nx*c+nz*s;N[i+2]=-nx*s+nz*c}return o},
  rza(a){const c=Math.cos(a),s=Math.sin(a);for(let i=0;i<P.length;i+=3){const x=P[i],y=P[i+1];P[i]=x*c-y*s;P[i+1]=x*s+y*c;const nx=N[i],ny=N[i+1];N[i]=nx*c-ny*s;N[i+1]=nx*s+ny*c}return o},
"""+a,1)
mark=" {const m=MB(),D=[52,56,52],L2=[84,88,80];m.box(0,-.2,.1,.5,.4,.8,D)"
i=s.index(mark);j=s.index("\n",i)
g=r"""
 {const K=[26,27,30],D=[40,43,49],P2=[78,84,92],L=[118,124,132],BR=[150,116,70],RD=[205,46,40],m=MB();
  const leg=(phi)=>{const l=MB(),hr=2.0,yh=2.5;
   const u=MB();u.box(1.4,-.4,0,2.8,.8,.8,P2).rza(.62);u.mv(hr,yh,0);l.cat(u);
   const kx=hr+2.8*Math.cos(.62),ky=yh+2.8*Math.sin(.62);
   const kn=MB();kn.cyl(0,-.45,0,.6,.9,BR,8).rx().mv(kx,ky,0);l.cat(kn);
   const w=MB();w.box(1.9,-.35,0,3.8,.7,.7,D).rza(-1.12);w.mv(kx,ky,0);l.cat(w);
   const fx=kx+3.8*Math.cos(1.12),fy=ky-3.8*Math.sin(1.12);
   const ft=MB();ft.cyl(0,0,0,.55,.9,K,6,.08).mv(fx,Math.max(0,fy)-.0,0);l.cat(ft);
   const st=MB();st.box(.6,-.18,0,1.4,.36,.36,RD).rza(-1.12).mv(kx+.3,ky-.1,.45);l.cat(st);
   l.ry(phi);return l};
  for(let k=0;k<4;k++)m.cat(leg(k*Math.PI/2+Math.PI/4));
  m.cyl(0,2.0,0,2.5,.9,D,8).cyl(0,2.9,0,2.1,.45,P2,8).cyl(0,3.35,0,1.6,.4,D,8);
  const tr=MB();tr.torus(0,0,0,2.55,.16,RD,20,6).mv(0,2.45,0);m.cat(tr);
  m.cyl(0,3.7,-.3,1.5,.7,P2,14).cyl(0,4.4,-.3,1.5,.8,P2,14,.9);
  m.box(0,5.0,-.9,.85,.42,.6,RD).box(0,5.05,-1.25,.5,.16,.12,[255,190,130]);
  for(const sx of[-1,1])m.box(sx*1.15,3.9,-.2,.5,1.0,2.0,D);
  m.box(0,3.5,-1.6,1.0,.9,1.4,P2);
  m.box(0,3.93,-1.6,.6,.26,7.6,L).box(0,3.51,-1.6,.6,.26,7.6,L).box(0,3.77,-1.6,.7,.16,7.7,[255,70,48]);
  for(let k=0;k<6;k++){const z=-4.6+k*1.2;m.box(0,4.19,z,.82,.1,.4,BR).box(0,3.41,z,.82,.1,.4,BR).box(.36,3.51,z,.1,.68,.4,BR).box(-.36,3.51,z,.1,.68,.4,BR)}
  m.box(0,3.45,-5.6,.8,.78,.6,D).box(0,3.85,-5.92,.4,.1,.12,[255,200,150]);
  m.box(0,3.55,2.35,.7,.6,.4,D);
  m.cyl(0,5.2,.2,.28,.4,K,8).box(0,5.6,.2,1.0,.6,1.0,D).box(0,6.2,.2,.9,.12,.9,P2);
  const lens=MB();lens.cyl(0,-.3,0,.3,.55,K,10).rx().mv(0,5.9,-.55);m.cat(lens);
  const gl2=MB();gl2.cyl(0,-.05,0,.2,.2,[120,225,255],10).rx().mv(0,5.9,-1.05);m.cat(gl2);
  m.box(.42,6.35,.2,.22,.2,.22,RD).box(-.42,6.35,.2,.22,.2,.22,L);
  {const F={'З':['111','001','011','001','111'],'А':['010','101','111','101','101'],'В':['110','101','110','101','110'],'Е':['111','100','110','100','111'],'Т':['111','010','010','010','010']},W='ЗАВЕТ',TC=[228,228,214];
   for(const sx of[-1,1])for(let li=0;li<5;li++)for(let r=0;r<5;r++)for(let c=0;c<3;c++){if(F[W[li]][r][c]!=='1')continue;const u=(c+li*4)*.1-.95,z=-.2+(sx>0?-u:u);m.box(sx*1.43,4.15+(4-r)*.1,z,.07,.1,.1,TC)}}
  m.cyl(.9,4.6,1.0,.07,1.8,K,6).box(.84,6.35,.94,.12,.12,.12,RD);
  G.guardian=m.build()}"""
s=s[:j]+g+s[j:]
open('/tmp/g3/index_dbg2.html','w').write(s)
